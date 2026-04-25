"""Método main"""
from calculadora import calcular

def main():
    """Executa a aplicação"""
    a = 1
    b = 2
    operacao = "3"

    resultado = calcular(a, b, operacao)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
