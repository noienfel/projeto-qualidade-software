"""Regras de negócio do LocalEats usadas nos testes unitários."""


def pedido_atingiu_valor_minimo(valor_pedido: float) -> bool:
    """Verifica se o pedido atingiu o valor mínimo de R$ 30,00.

    Args:
        valor_pedido: Valor total do pedido em reais.

    Returns:
        True se o valor for maior ou igual a 30; False caso contrário.

    Raises:
        ValueError: Se o valor do pedido for negativo.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= 30
