from llm_cliente import gerar_resposta
import json

CATEGORIAS = ["Suporte", "Vendas", "Financeiro", "Geral"]

def classificar_mensagem(mensagem, temperature=0.2):
    prompt = f"""
        Classifique a seguinte mensagem do cliente em uma das seguintes categorias: {', '.join(CATEGORIAS)}.
        Retorne apenas um JSON no formato:
        {{
            "categoria": "nome_categoria"
        }}
        
        Mensagem: "{mensagem}"
    """

    try:
        resposta = gerar_resposta(prompt, temperature)
        # Verifica se a resposta é um JSON válido
        data = json.loads(resposta)
        if "categoria" not in data:
            raise ValueError("Resposta da API não contém o campo 'categoria'.")
        return resposta
    except (json.JSONDecodeError, ValueError) as e:
        # Retorna um JSON de erro em caso de falha
        return json.dumps({"categoria": "Erro", "mensagem": str(e)})