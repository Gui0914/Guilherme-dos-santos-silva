def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

print("Calculadora Simples")
print("-------------------")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = input("Digite o número da operação desejada: ")

if opcao == "1":
    resultado = adicao(num1, num2)
    print("Resultado:", resultado)
elif opcao == "2":
    resultado = subtracao(num1, num2)
    print("Resultado:", resultado)
elif opcao == "3":
    resultado = multiplicacao(num1, num2)
    print("Resultado:", resultado)
elif opcao == "4":
    resultado = divisao(num1, num2)
    print("Resultado:", resultado)
else:
    print("Opção inválida.")

