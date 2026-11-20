# SETS "Conjuntos"
# Coleção mutável 
# Não garante ordem 
# Não há indice 
# Não permite elementos duplicados 

# Criar sets vazios 
dias = set()
dias.add('segunda')
dias.add('terça')
print(dias)

# Conjuntos inicializados
frutas = {'Maça', 'Uva', 'Pera', 'Laranja'}
frutas.discard(frutas)
print(frutas)
print(type(frutas))

print(len(frutas))

# # Converter lista para sets
# lista = [5, 7, 4, 1, 2, 8 ,13 ,6]
# conjunto_set = set(lista)  > SET não aceita repetição 
# print(conjunto_set)

numeros = [5, 7, 4, 1, 4, 8 , 13, 6, 5, 5, 13, 8, 29]
conjunto = set(numeros)  # converter lista para conjunto set 
print(len(conjunto)) # converte conjunto set para lista 
print(conjunto) 