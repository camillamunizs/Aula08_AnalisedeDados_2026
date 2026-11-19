numeros = []

while True:
    numero = int(input('\nInforme o número: '))
    numeros.append(numero)


    resposta = input('Quer continuar? [S/N] ').upper()

    if resposta == 'N':
       break


quantidade = len(numeros)
print(f'\nTotal de elementos: {quantidade}')
