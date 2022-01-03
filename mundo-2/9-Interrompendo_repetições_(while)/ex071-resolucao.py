# Exercício Python 71 - Simulador de Caixa Eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
cedulaatual = 50
totalcedulas = 0
while True:
    if total >= cedulaatual:
        total -= cedulaatual
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédulas de R${cedulaatual}.')
        if cedulaatual == 50:
            cedulaatual = 20
        elif cedulaatual == 20:
            cedulaatual = 10
        elif cedulaatual == 10:
            cedulaatual = 1
        totalcedulas = 0
        if total == 0:
            break
