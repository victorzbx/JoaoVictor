# Crie um programa que receba do usuario entradas numéricas inteiras e armazene-as em uma lista. Percorra os itens e conte quantos são pares e quantos são ímpares.
numeros = []
pares = []
impares = []
for n in range(5):
    num_escolhido = int(input("Digite um número: "))
    numeros.append(num_escolhido)

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else: 
        impares.append(num)

print(f"Há {len(pares)} números pares.")
print(f"Há {len(impares)} números ímpares.")

# # Combine duas listas separadas em uma única lista unificada.
#  # Números pares de 1 a 10:
num_par = [0, 2, 4, 6, 8]
#  # Números ímpares de 1 a 10:
num_impar = [1, 3, 5, 7, 9]
num_juntos = num_par + num_impar
print(f"A junção das duas listas forma a sequência: {num_juntos}")

# # Crie um programa que receba palavras inseridas pelo usuário e armazene-as em uma lista de strings. Identifique qual string possui o maior número de caracteres.
palavras = []
palavra_maior = ""
for n in range(5):
    palavra_escolhida = input("Digite uma palavra: ")
    palavras.append(palavra_escolhida)
    if n == 0:
        palavra_maior = palavra_escolhida
    elif len(palavra_escolhida) > len(palavra_maior):
        palavra_maior = palavra_escolhida
print(f"A maior palavra é: {palavra_maior} com {len(palavra_maior)} caractéres.")