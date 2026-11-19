numeros = []

for i in range (12): 
    numero = int(input('Informe o número: '))
    numeros.append(numero)

    ordenada = sorted(numeros)

print(f'Lista Ordenada: {ordenada}')
