#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
 numero = int(input("Digite um numero inteiro: "))
 if numero > 0:
    print("Positivo")
 elif numero < 0:
    print("Negativo")
 else:
    print("zero")
 if numero % 2 == 0:
    print("Par")
 else:
    print("Impar")
except ValueError:
 print("Por favor, digite um número inteiro válido")
