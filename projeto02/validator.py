import json

# Lista permitida de categorias
ALLOWED_CATEGORIES = ["Suporte", "Vendas", "Financeiro", "Geral", "Erro"]

def parse_json(input_data):
    """
    Tenta fazer o parsing do JSON e retorna o objeto Python correspondente.
    Lança uma exceção se o JSON for inválido.
    """
    try:
        return json.loads(input_data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro ao decodificar JSON: {e}")

def validate_json(data):
    """
    Valida se o JSON contém uma categoria permitida.
    """
    if "categoria" not in data:
        raise ValueError("JSON não contém o campo 'categoria'.")

    if data["categoria"] not in ALLOWED_CATEGORIES:
        raise ValueError(f"Categoria '{data['categoria']}' não é permitida.")

def error_json():
    """
    Retorna um JSON de erro padrão.
    """
    return {"status": "erro", "mensagem": "JSON inválido ou categoria não permitida."}