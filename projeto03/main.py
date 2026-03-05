from llm_cliente import LLMClient
from validator import validate_json, detectar_prompt_injection
from prompt import build_system_prompt
from retriever import gerar_embeddings, busca_por_similaridade

# Carregar embeddings no início do programa
conteudo, embeddings = gerar_embeddings("projeto03/conhecimento.txt")

def main():
    provider = input("Escolha o provider (openai/groq): ").strip().lower()
    cliente = LLMClient(provider=provider)

    while True:
        consulta_usuario = input("Digite sua pergunta (ou 'sair' para encerrar): ").strip()
        if consulta_usuario.lower() == "sair":
            break

        # Verificar tentativa de prompt injection
        if detectar_prompt_injection(consulta_usuario):
            print("Erro: Tentativa de prompt injection detectada.")
            continue

        # Usar busca por similaridade para encontrar contexto relevante
        contexto = busca_por_similaridade(consulta_usuario, conteudo, embeddings)

        # Verificar se há contexto relevante
        if not contexto:
            print("Erro: Informações insuficientes para responder à pergunta.")
            continue

        system_prompt = build_system_prompt()
        resposta_texto = cliente.generate_text(system_prompt, "\n".join(contexto))

        try:
            valido, dados = validate_json(resposta_texto)
            if valido:
                print(f"Resposta: {dados['resposta']}")
        except ValueError as e:
            print(f"Erro de validação: {e}")

if __name__ == "__main__":
    main()