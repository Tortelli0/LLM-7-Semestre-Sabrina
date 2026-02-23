# Relatório de comparativo dos testes

Feito trocando a `temperature` no arquivo `llm_cliente.py` na linha 15, variando entre valores de 0.2 a 1.0. Nos testes feito A mensagem "Quero contratar o plano premium" está com a Categoria vazia, por isso a falha, assim sendo o erro algo proposital para testar o validador.

## Teste 1, Temperatura 0.2

### 100% de acertos
Erro ao processar mensagem: Quero contratar o plano premium
Erro: Categoria '' não é permitida.
Resposta de erro: {'status': 'erro', 'mensagem': 'JSON inválido ou categoria não permitida.'}

Cliente: O sistema está com erro
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Quero cancelar minha assinatura
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Quero falar com um atendente
Resposta: ```json
{
    "categoria": "Geral"
}
```

Cliente: Preciso de ajuda com meu pagamento
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Gostaria de atualizar minhas informações de conta
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Vocês trabalham no sábado
Resposta: ```json
{
    "categoria": "Geral"
}
```

## Teste 2, Temperatura 0.4

### 100% de acertos
Erro ao processar mensagem: Quero contratar o plano premium
Erro: Categoria '' não é permitida.
Resposta de erro: {'status': 'erro', 'mensagem': 'JSON inválido ou categoria não permitida.'}

Cliente: O sistema está com erro
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Quero cancelar minha assinatura
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Quero falar com um atendente
Resposta: ```json
{
    "categoria": "Geral"
}
```

Cliente: Preciso de ajuda com meu pagamento
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Gostaria de atualizar minhas informações de conta
Resposta: ```json
{
    "categoria": "Geral"
}
```

Cliente: Vocês trabalham no sábado
Resposta: ```json
{
    "categoria": "Geral"
}
```

## Teste 3, Temperatura 0.6

### 100% de acertos
Erro ao processar mensagem: Quero contratar o plano premium
Erro: Categoria '' não é permitida.
Resposta de erro: {'status': 'erro', 'mensagem': 'JSON inválido ou categoria não permitida.'}

Cliente: O sistema está com erro
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Quero cancelar minha assinatura
Resposta: ```json
{"categoria":"Financeiro"}
```

Cliente: Quero falar com um atendente
Resposta: ```json
{
    "categoria": "Geral"
}
```

Cliente: Preciso de ajuda com meu pagamento
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Gostaria de atualizar minhas informações de conta
Resposta: ```json
{
    "categoria": "Geral"
}
```

Cliente: Vocês trabalham no sábado
Resposta: ```json
{
    "categoria": "Geral"
}
```

## Teste 4, Temperatura 0.8

### 100% de acertos
Erro ao processar mensagem: Quero contratar o plano premium
Erro: Categoria '' não é permitida.
Resposta de erro: {'status': 'erro', 'mensagem': 'JSON inválido ou categoria não permitida.'}

Cliente: O sistema está com erro
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Quero cancelar minha assinatura
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Quero falar com um atendente
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Preciso de ajuda com meu pagamento
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Gostaria de atualizar minhas informações de conta
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Vocês trabalham no sábado
Resposta: ```json
{
    "categoria": "Geral"
}
```

## Teste 5, Temperatura 1.0

### 100% de acertos
Erro ao processar mensagem: Quero contratar o plano premium
Erro: Categoria '' não é permitida.
Resposta de erro: {'status': 'erro', 'mensagem': 'JSON inválido ou categoria não permitida.'}

Cliente: O sistema está com erro
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Quero cancelar minha assinatura
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Quero falar com um atendente
Resposta: ```json
{
    "categoria": "Geral"
}
```

Cliente: Preciso de ajuda com meu pagamento
Resposta: ```json
{
    "categoria": "Financeiro"
}
```

Cliente: Gostaria de atualizar minhas informações de conta
Resposta: ```json
{
    "categoria": "Suporte"
}
```

Cliente: Vocês trabalham no sábado
Resposta: ```json
{
    "categoria": "Geral"
}
```
