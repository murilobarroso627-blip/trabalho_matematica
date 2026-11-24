import math

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        print("Erro: Divisão por zero não é permitida.")
        return 0
    return a / b
def radiano(x):
    x = math.radians(x)
    return x
def seno(x):
    seno = math.sin(x)
    return seno
def cos(x):
    cos = math.cos(x)
    return cos
def hipotenusa(b, c):
    a = (b**2) + (c**2)
    a = a**0.5
    return a
def tangente(x):
    tangente = math.tan(x)
    return tangente


print("Olá! Bem-vindo à calculadora simples.")
resposta = int(input("Você deseja realizar uma operação?: "))
while resposta == 1:
    print("Oque você deseja fazer?")
    print("1 - Contas simples")
    print("2 - Trigonometria")
    area = int(input("Digite o número da operação desejada: "))
    match area:
        case 1:
            print("1 - Adição")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Sair")
            operacao = int(input("Digite o número da operação desejada: "))
            match operacao:
                case 1:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = soma(num1, num2)
                    print(f"O resultado da adição é: {resultado}")
                case 2:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = subtracao(num1, num2)
                    print(f"O resultado da subtração é: {resultado}")
                case 3:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = multiplicacao(num1, num2)
                    print(f"O resultado da multiplicação é: {resultado}")
                case 4:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = divisao(num1, num2)
                    print(f"O resultado da divisão é: {resultado}")
                case 5:
                    print("Saindo da calculadora. Até logo!")
                    break
        case 2:
            print("1 - Seno")
            print("2 - Cosseno")
            print("3 - Tangente")
            print("4 - Sair")
            operacao = int(input("Digite o número da operação desejada: "))
            match operacao:
                case 1:
                    angulo = float(input("Digite o ângulo em graus: "))
                    angulo_rad = radiano(angulo)
                    resultado = seno(angulo_rad)
                    print(f"O seno de {angulo}° é: {resultado}")
    resposta = int(input("Você deseja realizar outra operação? (1 - Sim, 0 - Não): "))
print("Obrigado por usar a calculadora!")