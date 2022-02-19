# Exercício Python 94 - Unindo dicionários e listas
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = dict()
cadastro = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROU! Escolha apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERROU! Resposta inválida.')
    if opcao == 'N':
        break
print('='*50)
print(f'Temos {len(cadastro)} pessoas cadastradas.')
media = soma / len(cadastro)
print(f'A média de idade é de {media:5.2f}')
print('As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Pessoas acima da média são ', end='')
for p in cadastro:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k}: {v}. ', end='')
        print()
print('FIM!')


