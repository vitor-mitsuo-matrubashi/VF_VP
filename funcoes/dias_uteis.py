import pandas as pd
from datetime import datetime, timedelta

# Define o caminho para o arquivo CSV
caminho_feriados = '../data/workdays.csv'


def ler_feriados(caminho_feriados: str) -> list:
    """
    Lê os feriados de um arquivo CSV e retorna uma lista de datas.

    Parâmetros:
    ----------
    caminho_feriados : str
        O caminho para o arquivo CSV que contém os feriados. O arquivo deve ter uma
        coluna chamada 'data' com as datas dos feriados no formato 'YYYY-MM-DD'.

    Retorna:
    -------
    list
        Uma lista de objetos datetime representando os feriados lidos do arquivo.

    Exceções:
    ---------
    FileNotFoundError
        Se o arquivo especificado não for encontrado.
    ValueError
        Se a coluna 'data' não estiver presente no arquivo CSV ou se não puder ser
        convertida para o formato datetime.

        """


    df = pd.read_csv(caminho_feriados)

    # Converte a coluna de datas para o tipo datetime
    feriados = pd.to_datetime(df['data']).tolist()

    return feriados

def dias_uteis(data_inicial: str, data_final: str, feriados: list) -> int:
    """
    Calcula a quantidade de dias uteis entre duas datas.

    Essa função recebe duas datas no formato 'YYYY-MM-DD' e calcula o número
    de dias uteis entre elas.

    Args:
        data_inicial (str): Data de início no formato 'YYYY-MM-DD'.
        data_final (str): Data de término no formato 'YYYY-MM-DD'.

    Returns:
        int: A quantidade de dias corridos entre as duas datas.

    Raises:
        ValueError: Se as datas estiverem em um formato inválido.


    """


    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')

    dias_uteis = 0
    data_atual = data_inicial

    while data_atual <= data_final:
        # Verifica se é um dia útil (não é sábado ou domingo e não é feriado)
        if data_atual.weekday() < 5 and data_atual not in feriados:
            dias_uteis += 1
        data_atual += timedelta(days=1)

    return dias_uteis