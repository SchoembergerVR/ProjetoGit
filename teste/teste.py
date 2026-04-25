import pytest
from src.calculadora import calcular

def test_soma():
    assert calcular(1, 2, "1") == 3

def test_subtracao():
    assert calcular(5, 2, "2") == 3

def test_multiplicacao():
    assert calcular(2, 3, "3") == 6

def test_divisao():
    assert calcular(10, 2, "4") == 5

def test_divisao_por_zero():
    assert calcular(10, 0, "4") == "Erro: divisão por zero"

def test_opcao_invalida():
    assert calcular(1, 2, "99") == "Opção inválida"
