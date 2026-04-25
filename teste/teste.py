"""Teste de código"""
from src.calculadora import calcular

def test_soma():
    """Teste soma"""
    assert calcular(1, 2, "1") == 3

def test_subtracao():
    """Teste subtração"""
    assert calcular(5, 2, "2") == 3

def test_multiplicacao():
    """Teste multiplicação"""
    assert calcular(2, 3, "3") == 6

def test_divisao():
    """Teste divisão"""
    assert calcular(10, 2, "4") == 5

def test_divisao_por_zero():
    """Teste divisão por zero"""
    assert calcular(10, 0, "4") == "Erro: divisão por zero"

def test_opcao_invalida():
    """Teste opção inválida"""
    assert calcular(1, 2, "99") == "Opção inválida"
