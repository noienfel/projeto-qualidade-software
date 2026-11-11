"""Testes unitários da regra de valor mínimo do pedido."""

import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo


# Responsável: Rafael
def test_pedido_com_valor_acima_do_minimo_retorna_true():
    """Pedido de R$ 50,00 deve atingir o valor mínimo."""
    assert pedido_atingiu_valor_minimo(50) is True


# Responsável: Rafael
def test_pedido_no_limite_minimo_retorna_true():
    """Pedido de exatamente R$ 30,00 deve ser aceito."""
    assert pedido_atingiu_valor_minimo(30) is True


# Responsável: Rafael
def test_pedido_abaixo_do_minimo_retorna_false():
    """Pedido de R$ 20,00 não deve atingir o valor mínimo."""
    assert pedido_atingiu_valor_minimo(20) is False


# Responsável: Rafael
def test_pedido_com_valor_negativo_gera_value_error():
    """Valor negativo deve ser rejeitado com ValueError."""
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-1)
