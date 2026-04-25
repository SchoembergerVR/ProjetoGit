def calcular(a, b, operacao):
    if operacao == "4" and b == 0:
        return "Erro: divisão por zero"
    elif operacao == "1":
        return a + b
    elif operacao == "2":
        return a - b
    elif operacao == "3":
        return a * b
    elif operacao == "4":
        return a / b
    else:
        return "Opção inválida"
