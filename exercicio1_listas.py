num = []
pares = []
impares = []

for n in range(10):
    numero = int(input("Digite um número para adicionar a lista: "))
    num.append(numero)

if numero % 2 == 0:
    pares.append(numero)
else:
    impares.append(numero)

print(f'''
A lista completa é: {num} 
A lista dos pares é: {pares}
A lista dos ímpares é: {impares}
''')