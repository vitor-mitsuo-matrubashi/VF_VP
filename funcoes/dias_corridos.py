from datetime import datetime

def dias_corridos(data_inicial: str, data_final: str) -> int:
    """
    Calcula a quantidade de dias corridos entre duas datas.

    Essa função recebe duas datas no formato 'YYYY-MM-DD' e calcula o número
    de dias corridos entre elas.

    Args:
        data_inicial (str): Data de início no formato 'YYYY-MM-DD'.
        data_final (str): Data de término no formato 'YYYY-MM-DD'.

    Returns:
        int: A quantidade de dias corridos entre as duas datas.

    Raises:
        ValueError: Se as datas estiverem em um formato inválido.

    Example:
        >>> dias_corridos('2024-01-01', '2024-01-10')
        9
    """


    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')
    return (data_final - data_inicial).days


dias = dias_corridos('2024-09-16','2024-11-04')

print(f"A quantidade de dias corridos desde o dia do acidente foi {dias} dias")