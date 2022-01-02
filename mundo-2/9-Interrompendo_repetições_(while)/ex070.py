# Exercício Python 70 - Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

cont = 1
maisbarato = mais1k = total = 0
produtobarato = opcao = ' '
while opcao not in 'Nn':
    produto = str(input('Digite o nome do produto: ')).title()
    valor = float(input('Digite o preço: '))

    if cont == 1 or valor < maisbarato:
        maisbarato = valor
        produtobarato = produto

    total += valor
    if valor > 1000:
        mais1k += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja inserir outro produto? [S/N] -> ')).upper().strip()[0]
    cont += 1
print(f'''
O total da compra foi: R${total}
{mais1k} produto(s) tem o seu valor superior a R$1.000,00.
E o produto mais barato foi {produtobarato}.
''')
