def calcular_estoque(quantidade, preco):
    """Calcula o valor total do estoque."""
    if quantidade < 0 or preco < 0:
        raise ValueError("Valores inválidos")

    return quantidade * preco
