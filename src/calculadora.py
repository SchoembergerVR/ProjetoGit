"""Operações básicas de calculadora"""
def calcular(a, b, operacao):
    if operacao == "4" and b == 0:
        return "Erro: divisão por zero"
    if operacao == "1":
        return a + b
    if operacao == "2":
        return a - b
    if operacao == "3":
        return a * b
    if operacao == "4":
        return a / b

    return "Opção inválida"
