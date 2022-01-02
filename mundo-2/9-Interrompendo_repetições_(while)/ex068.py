# Exercício Python #8 - Jogo do Par ou Ímpar
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('~~~ PAR OU ÍMPAR ~~~')

i = 0
while True:
    print('\n')
    num = int(input('Digite seu número: '))

    p_ou_i = ' '
    while p_ou_i not in 'PpIi':
        p_ou_i = str(input('Par ou ímpar? [P/I]: ')).upper()

    pc = randint(1, 9)
    soma = pc + num

    if p_ou_i == 'P':

        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            print(f'Você escolheu {num} e o PC {pc}. \nA soma dos valores é um número PAR: {soma}.')
            i += 1
        else:
            print('VOCÊ PERDEU!')
            print(f'Você escolheu {num} e o PC {pc}. \nA soma dos valores é um número ÍMPAR: {soma}.')
            break
    else:
        if soma % 2 != 0:
            print('VOCÊ VENCEU!')
            print(f'Você escolheu {num} e o PC {pc}. \nA soma dos valores é um número ÍMPAR: {soma}.')
            i += 1
        else:
            print('VOCÊ PERDEU!')
            print(f'Você escolheu {num} e o PC {pc}. \nA soma dos valores é um número PAR: {soma}.')
            break
print(f'\n === Você venceu {i}x ===')
