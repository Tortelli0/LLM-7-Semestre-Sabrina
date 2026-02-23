from classifier import classificar_mensagem

mensagens_cliente = [
    "Quero contratar o plano premium",
    "O sistema está com erro",
    "Quero cancelar minha assinatura",
    "Quero falar com um atendente",
    "Preciso de ajuda com meu pagamento",
    "Gostaria de atualizar minhas informações de conta",
    "Vocês trabalham no sábado",
]

for mensagens in mensagens_cliente:
    reposta = classificar_mensagem(mensagens)
    print(f"Cliente: {mensagens}")
    print(f"Resposta: {reposta}\n")