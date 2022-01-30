# Exercício Python 84 - Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro = list()
dados = list()
nomepesados = list()
nomeleves = list()
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso KG: ')))
    cadastro.append(dados[:])
    dados.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N]: '))
        if opcao in 'NnSs':
            break
    if opcao in 'Nn':
        break
print()
print(f'Foram cadastrados {len(cadastro)} pessoas.')
pesado = leve = cadastro[0][1]
for pessoa in cadastro:
    if pessoa[1] > pesado:
        pesado = pessoa[1]
    if pessoa[1] < leve:
        leve = pessoa[1]
for pessoa in cadastro:
    if pessoa[1] == pesado:
        nomepesados.append(pessoa[0])
    if pessoa[1] == leve:
        nomeleves.append(pessoa[0])
print(f'A pessoa(s) mais leve(s) tem {leve}kg: {nomeleves}')
print(f'E a pessoa(s) mais pesada(s) tem {pesado}kg: {nomepesados}')
