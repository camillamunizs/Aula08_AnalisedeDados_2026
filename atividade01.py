vendas = []

for i in range (10): 
    venda = float(input('Informe o valor da venda R$: '))
    vendas.append(venda)
    total = sum(vendas)

print(f'Total R$: {total:.2f}')


