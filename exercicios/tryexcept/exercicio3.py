#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

n1 = int(input("Digite o primeiro numero: "))
ope = input("Digite algum operador(+, -, *, /): ")
n2 = int(input("Digite o segundo numero: "))

try:
    if ope == "+":
        resultado = n1 + n2
    elif ope == "-":
        resultado = n1-n2
    elif ope == "*":
        resultado = n1*n2
    elif ope == "/":
        resultado = n1/n2
    else:
        print("valor invalido")
    print("Resultado: ", resultado)
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")
