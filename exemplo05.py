# TUPLAS 
# Coleção imutável 
# Permite elementos duplicados 
# Permite acesso pelo índice 
# Mantém ordem de inserção 

frutas = ('Maça', 'Uva', 'Pera', 'Laranja')
print(frutas[1])
print(frutas)

#frutas[1] = 'Melancia' # A tupla não pode ser alterada

numeros = (10, 20, 50, 20, 30, 10, 400, 20)
print(numeros.count(20))  #COUNT conta quantas vezes o elemento informado aparece 
print(frutas.index('Laranja'))  #INDEX mostra a posição do elemento informado. 

