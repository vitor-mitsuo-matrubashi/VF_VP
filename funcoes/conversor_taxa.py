def converter_taxa_ano_para_dia(taxa_ano: float, tipo_calculo: str, dias_no_ano: int = 365) -> float:
    """
    Converte uma taxa anual para uma taxa diária, com base no tipo de cálculo (linear ou exponencial).

    Parâmetros:
    ----------
    taxa_ano : float
        A taxa anual no formato decimal (por exemplo, 0.05 para 5%).
    tipo_calculo : str
        Tipo de cálculo. Pode ser 'linear' ou 'exponencial'.
    dias_no_ano : int, opcional
        Número de dias no ano. O padrão é 365 dias. Use 252 dias para o mercado financeiro.

    Retorna:
    -------
    float
        A taxa diária no formato decimal.

    Exceções:
    ---------
    ValueError
        Se o tipo_calculo não for 'linear' ou 'exponencial'.
    """

    if tipo_calculo == 'linear':
        # Cálculo linear: A taxa diária é simplesmente a taxa anual dividida pelos dias no ano
        taxa_diaria = taxa_ano / dias_no_ano

    elif tipo_calculo == 'exponencial':
        # Cálculo exponencial: A fórmula para converter a taxa anual para a taxa diária
        taxa_diaria = (1 + taxa_ano) ** (1 / dias_no_ano) - 1

    else:
        raise ValueError("O tipo_calculo deve ser 'linear' ou 'exponencial'.")

    return taxa_diaria


# Exemplo de uso:
# taxa_ano = 0.05  # 5% ao ano
# tipo_calculo = 'exponencial'  # Pode ser 'linear' ou 'exponencial'
# taxa_diaria = converter_taxa_ano_para_dia(taxa_ano, tipo_calculo)
#
# print(f"A taxa diária é: {taxa_diaria:.6f}")


def converter_taxa_mes_para_dia(taxa_mes: float, tipo_calculo: str, dias_no_mes: int = 30) -> float:
    """
    Converte uma taxa mensal para uma taxa diária, com base no tipo de cálculo (linear ou exponencial).

    Parâmetros:
    ----------
    taxa_mes : float
        A taxa mensal no formato decimal (por exemplo, 0.05 para 5%).
    tipo_calculo : str
        Tipo de cálculo. Pode ser 'linear' ou 'exponencial'.
    dias_no_mes : int, opcional
        Número de dias no mês. O padrão é 30 dias.

    Retorna:
    -------
    float
        A taxa diária no formato decimal.

    Exceções:
    ---------
    ValueError
        Se o tipo_calculo não for 'linear' ou 'exponencial'.
    """

    if tipo_calculo == 'linear':
        # Cálculo linear: A taxa diária é simplesmente a taxa mensal dividida pelos dias no mês
        taxa_diaria = taxa_mes / dias_no_mes

    elif tipo_calculo == 'exponencial':
        # Cálculo exponencial: A fórmula para converter a taxa mensal para a taxa diária
        taxa_diaria = (1 + taxa_mes) ** (1 / dias_no_mes) - 1

    else:
        raise ValueError("O tipo_calculo deve ser 'linear' ou 'exponencial'.")

    return taxa_diaria


# Exemplo de uso:
# taxa_mes = 0.05  # 5% ao mês
# tipo_calculo = 'exponencial'  # Pode ser 'linear' ou 'exponencial'
# taxa_diaria = converter_taxa_mes_para_dia(taxa_mes, tipo_calculo)
#
# print(f"A taxa diária é: {taxa_diaria:.6f}")
