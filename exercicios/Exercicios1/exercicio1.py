
try:
    valor = int(input("Escreva o valor em graus: "))
    if valor < 18:
        print("baixa")
    elif 18 <= valor <= 20:
        print("media")
    else:
        print("Alta")
except ValueError:
    print("insera apenas numeros inteiros")