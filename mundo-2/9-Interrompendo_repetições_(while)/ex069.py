# Exercício Python 69 - Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

continuar = 'S'
mulher20 = homem = maior = 0
while continuar != 'N':
    while True:
        idade = input(f'\nDigite a idade: ')
        try:
            idade = int(idade)
            if idade >= 18:
                maior += 1
            break
        except ValueError:
            continue

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            homem += 1
        else:
            if idade <= 20:
                mulher20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()

if maior == 1:
    print(f'\n{maior} pessoa é maior de idade.')
else:
    print(f'\n{maior} pessoas são maiores de idades.')

    if homem == 1:
        print(f'Foi cadastrado {homem} homem.')
    else:
        print(f'Foram cadastrados {homem} homens.')

    if mulher20 == 1:
        print(f'E teve o cadastrado de {mulher20} mulher com menos de 20 anos.')
    else:
        print(f'E teve o cadastrado de {mulher20} mulheres com menos de 20 anos.')
