"""Calculadora"""
def calcular(a, b, operacao):
    """Operações básicas de calculadora"""
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
