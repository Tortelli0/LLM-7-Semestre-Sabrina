from llm_cliente import gerar_resposta

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

    resposta = gerar_resposta(prompt, temperature)
    return resposta