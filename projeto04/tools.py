import datetime
from typing import Tuple


def data_atual():
    return datetime.date.today()


def parse_date_string(date_str: str) -> Tuple[int, int, int]:
    """Tenta parsear datas nos formatos YYYY-MM-DD ou DD/MM/YYYY.
    Retorna tupla (ano, mes, dia) ou levanta ValueError se inválido.
    """
    date_str = date_str.strip()
    # YYYY-MM-DD
    if "-" in date_str:
        parts = date_str.split("-")
        if len(parts) == 3:
            y, m, d = parts
            return int(y), int(m), int(d)
    # DD/MM/YYYY
    if "/" in date_str:
        parts = date_str.split("/")
        if len(parts) == 3:
            d, m, y = parts
            return int(y), int(m), int(d)
    raise ValueError("Formato de data não reconhecido")
