produtos = []    # listas é plural 

for i in range (3):
    produto = input('Informe o nome do produto: ')
    produtos.append(produto) # adiciona na lista produtos 

print(produtos)

# Acesso ao elemento 
n = int(input('Digite o índice do elemento a acessar: '))
print(produtos[n-1])  # numera a lista a partir de 1,2,3.. senão começa a contar a partir do ZERO 

# Alterando uma lista "nome de um elemento"
produtos[n-1] = input(f'Informe o nome do outro elemento na posição {n}: ')
print(produtos)

# Remover da lista
produto_a_remover = input('\n Digite o nome do produto a remover: ')
produtos.remove(produto_a_remover)
print(produtos)

if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print(produtos)
