#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

palavra = input("Digite a palavra: ")
if isinstance(palavra, str):
    format = palavra.replace("", " ").lower()
    if format == format[::-1]:
        print("é um palindromo")
        print(palavra)
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
