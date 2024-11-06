from datetime import datetime

def calcular_dias_corridos(data_inicial: str, data_final: str) -> int:
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
        # >>> dias_corridos('2024-01-01', '2024-01-10')
        9
    """


    # Remove qualquer hora da string de data
    data_inicial = data_inicial.split(' ')[0]
    data_final = data_final.split(' ')[0]

    # Converte as strings de data para objetos datetime
    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')

    return (data_final - data_inicial).days


# print(calcular_dias_corridos('2024-10-10', '2024-12-30'))