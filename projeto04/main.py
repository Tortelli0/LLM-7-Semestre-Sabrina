from openai import OpenAI
from dotenv import load_dotenv
from tools import data_atual, parse_date_string
import os
import json
import re
import datetime

load_dotenv()

# Configurar cliente para usar GROQ (compatível com OpenAI via base_url)
groq_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
if not groq_key:
    print("Aviso: nenhuma chave GROQ_API_KEY/OPENAI_API_KEY encontrada no .env")
client = OpenAI(api_key=groq_key, base_url="https://api.groq.com/openai/v1")
# Modelo a ser usado com Groq (pode ser configurado via .env)
MODEL = os.getenv("GROQ_MODEL", os.getenv("OPENAI_MODEL", "llama-3.1-8b-instant"))

# Arquivo para persistir histórico
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "history.json")

# Persona do assistente (mensagem de sistema)
SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "Você é um assistente em português, educado, objetivo e levemente bem-humorado. "
        "Responda em frases curtas e claras, peça esclarecimentos se necessário."
    ),
}


# Histórico de mensagens para manter o contexto da conversa
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    # Garantir que a mensagem de sistema exista
                    if not data or data[0].get("role") != "system":
                        return [SYSTEM_MESSAGE] + data
                    return data
        except Exception:
            pass
    return [SYSTEM_MESSAGE]


def save_history(hist):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(hist, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Erro salvando histórico:", e)


historico_mensagens = load_history()


def trim_history(max_messages=10):
    # Mantém a mensagem de sistema e as últimas `max_messages` mensagens
    system = historico_mensagens[0] if historico_mensagens else SYSTEM_MESSAGE
    rest = historico_mensagens[1:]
    if len(rest) > max_messages:
        rest = rest[-max_messages:]
    historico_mensagens[:] = [system] + rest


def salvar_historico(mensagem):
    historico_mensagens.append(mensagem)
    trim_history(max_messages=10)
    save_history(historico_mensagens)


# --- Funções Python integradas ---
def calcular_idade(data_nascimento_str: str) -> str:
    try:
        y, m, d = parse_date_string(data_nascimento_str)
        born = datetime.date(y, m, d)
        today = datetime.date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return f"A idade é {age} anos (nascido em {born.isoformat()})."
    except Exception:
        return "Não consegui interpretar a data. Use YYYY-MM-DD ou DD/MM/YYYY."


def converter_temperatura(text: str) -> str:
    # Procura números e unidades
    m = re.search(r"(-?\d+(?:[\.,]\d+)?)\s?°?\s?([cCfF])", text)
    if not m:
        return "Não detectei temperatura com unidade (ex: 37C ou 98F)."
    val = float(m.group(1).replace(',', '.'))
    unit = m.group(2).upper()
    if unit == "C":
        f = (val * 9/5) + 32
        return f"{val}°C = {round(f,2)}°F"
    else:
        c = (val - 32) * 5/9
        return f"{val}°F = {round(c,2)}°C"


def detect_and_call_function(pergunta: str):
    # Detecta necessidade de função por regras simples
    # Idade: procura 'idade' e uma data
    if "idade" in pergunta.lower():
        # tenta extrair data no formato YYYY-MM-DD ou DD/MM/YYYY
        m = re.search(r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})", pergunta)
        if m:
            return calcular_idade(m.group(1))
    # Converter temperatura
    if re.search(r"°|celsius|fahrenheit|c\b|f\b", pergunta.lower()):
        return converter_temperatura(pergunta)
    return None


def chat(pergunta):
    # Comando especial /limpar
    if pergunta.strip().lower() == "/limpar":
        historico_mensagens[:] = [SYSTEM_MESSAGE]
        save_history(historico_mensagens)
        return "Memória da conversa apagada."

    # Checa se alguma função deve ser chamada
    func_result = detect_and_call_function(pergunta)
    if func_result:
        salvar_historico({"role": "user", "content": pergunta})
        salvar_historico({"role": "assistant", "content": func_result})
        return func_result

    salvar_historico({"role": "user", "content": pergunta})

    try:
        # Usar endpoint compatível com Groq: responses.create
        resp = client.responses.create(
            model=MODEL,
            input=historico_mensagens
        )
        # Extrair texto de forma robusta
        if hasattr(resp, "output_text") and resp.output_text:
            resposta_conteudo = resp.output_text
        else:
            try:
                resposta_conteudo = resp.output[0].content[0].text
            except Exception:
                resposta_conteudo = str(resp)
    except Exception as e:
        resposta_conteudo = f"Erro ao consultar a API: {e}"

    salvar_historico({"role": "assistant", "content": resposta_conteudo})
    return resposta_conteudo


def print_help():
    print("Comandos:")
    print("  /limpar    - Apaga a memória da conversa")
    print("  sair/exit  - Encerra o chat")
    print("Exemplos de uso das funções: 'Qual minha idade se nasci em 1990-05-20?', 'Converter 37C para F')")


if __name__ == '__main__':
    print("Chat iniciado. Digite suas mensagens. Digite /limpar para apagar memória.")
    print_help()
    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chat. Até mais!")
            break

        if "data" in pergunta.lower():
            salvar_historico({"role": "user", "content": pergunta})
            resposta = "Hoje é " + str(data_atual())
            salvar_historico({"role": "assistant", "content": resposta})
            print("Assistente: " + resposta)
            continue

        resposta = chat(pergunta)
        print("Assistente: ", resposta)
