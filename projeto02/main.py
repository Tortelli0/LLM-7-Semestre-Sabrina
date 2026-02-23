from classifier import classificar_mensagem
from validator import parse_json, validate_json, error_json
import json

mensagens_cliente = [
    "Quero contratar o plano premium",
    "O sistema está com erro",
    "Quero cancelar minha assinatura",
    "Quero falar com um atendente",
    "Preciso de ajuda com meu pagamento",
    "Gostaria de atualizar minhas informações de conta",
    "Vocês trabalham no sábado",
]

for mensagem in mensagens_cliente:
    try:
        # Classificação da mensagem para gerar a categoria
        resposta_classificacao = classificar_mensagem(mensagem)
        
        # Converte a resposta da classificação em JSON
        data = parse_json(resposta_classificacao)

        # Validação do JSON gerado
        validate_json(data)

        print(f"Cliente: {mensagem}")
        print(f"Resposta: {resposta_classificacao}\n")
    except ValueError as e:
        # Tratamento de erro e retorno de JSON de erro
        print(f"Erro ao processar mensagem: {mensagem}")
        print(f"Erro: {e}")
        print(f"Resposta de erro: {error_json()}\n")