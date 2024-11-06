from datetime import datetime
from funcoes.dias_corridos import calcular_dias_corridos
from funcoes.conversor_taxa import converter_taxa_ano_para_dia, converter_taxa_mes_para_dia

# Supondo que essas funções já existam:
# def calcular_dias_corridos(data_inicial: str, data_final: str) -> int:
# def converter_taxa_ano_para_dia(taxa_ano: float, tipo_calculo: str, dias_no_ano: int = 365) -> float:
# def converter_taxa_mes_para_dia(taxa_mes: float, tipo_calculo: str, dias_no_mes: int = 30) -> float:

def calcular_vf(notional: float, tipo_calculo: str, taxa: float, data_inicial: str, data_final: str, tipo_taxa: str) -> float:
    """
    Calcula o Valor Futuro (VF) com base nos dados fornecidos.

    Parâmetros:
    ----------
    notional : float
        O valor inicial da operação.
    tipo_calculo : str
        O modelo de cálculo da taxa ('exponencial' ou 'linear').
    taxa : float
        A taxa no formato decimal (por exemplo, 0.05 para 5%).
    data_inicial : str
        Data inicial no formato 'YYYY-MM-DD'.
    data_final : str
        Data final no formato 'YYYY-MM-DD'.
    tipo_taxa : str
        Tipo de taxa fornecida ('ano', 'mes' ou 'dia').

    Retorna:
    -------
    float
        O Valor Futuro (VF) calculado.
    """
    # Converte as datas de string para datetime
    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')

    # Calcula o número de dias corridos no período
    dias_corridos = calcular_dias_corridos(str(data_inicial), str(data_final))

    # Converte a taxa para o formato diário, se necessário
    if tipo_taxa == 'ano':
        taxa_diaria = converter_taxa_ano_para_dia(taxa, tipo_calculo)
    elif tipo_taxa == 'mes':
        taxa_diaria = converter_taxa_mes_para_dia(taxa, tipo_calculo)
    elif tipo_taxa == 'dia':
        taxa_diaria = taxa
    else:
        raise ValueError("O tipo de taxa deve ser 'ano', 'mes' ou 'dia'.")

    # Cálculo do Valor Futuro (VF)
    if tipo_calculo == 'linear':
        vf = notional * (1 + taxa_diaria * dias_corridos)
    elif tipo_calculo == 'exponencial':
        vf = notional * (1 + taxa_diaria) ** dias_corridos
    else:
        raise ValueError("O tipo_calculo deve ser 'exponencial' ou 'linear'.")

    return vf


# Exemplo de uso:
def obter_dados_usuario():
    notional = float(input("Informe o Notional da operação: "))
    data_inicial = input("Informe a data inicial (YYYY-MM-DD): ")
    data_final = input("Informe a data final (YYYY-MM-DD): ")
    taxa = float(input("Informe a taxa (em formato decimal, por exemplo 0.05 para 5%): "))
    tipo_taxa = input("Informe o tipo de taxa (ano, mes ou dia): ").lower()
    tipo_calculo = input("Informe o modelo de cálculo (exponencial ou linear): ").lower()

    return notional, data_inicial, data_final, taxa, tipo_taxa, tipo_calculo


# Exemplo de execução:
notional, data_inicial, data_final, taxa, tipo_taxa, tipo_calculo = obter_dados_usuario()
resultado = calcular_vf(notional, tipo_calculo, taxa, data_inicial, data_final, tipo_taxa)

print(f"O Valor Futuro (VF) é: {resultado:.2f}")
