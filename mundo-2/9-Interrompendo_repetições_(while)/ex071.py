# Exercício Python 71 - Simulador de Caixa Eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('Qual valor (inteiro) deseja sacar? R$'))
# range(start, stop, step)
while True:
    i = soma50 = saque50 = 0
    for i in range(49, saque, 50):
        saque50 += 1
    resta50 = saque - (saque50 * 50)
    print(f'{saque50} nota(s) de R$50')
    if resta50 == 0:
        break
    ################################################
    i = soma20 = saque20 = 0
    for i in range(19, resta50, 20):
        saque20 += 1
    resta20 = resta50 - (saque20 * 20)
    print(f'{saque20} nota(s) de R$20')
    if resta20 == 0:
        break
    ################################################
    i = soma10 = saque10 = 0
    for i in range(9, resta20, 10):
        saque10 += 1
    resta10 = resta20 - (saque10 * 10)
    print(f'{saque10} nota(s) de R$10')
    if resta10 == 0:
        break
    ################################################
    i = soma1 = saque1 = 0
    for i in range(0, resta10, 1):
        saque1 += 1
    resta1 = resta10 - (saque1 * 1)
    print(f'{saque1} nota(s) de R$1')
    if resta1 == 0:
        break

print('Saque realizado com sucesso.')
