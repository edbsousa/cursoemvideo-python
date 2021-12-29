# Exercício Python 58 - Jogo da Adivinhação v2.0
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randrange

num = randrange(0, 10, 1)

print('=-=' * 20)

tentativas = 1

num_user = int(input(f'O computador “pensou” em um número inteiro entre 0 e 10.'
                     f'\nTente adivinhar: '))

while num_user != num:
    tentativas += 1
    if num_user > num:
        num_user = int(input('ERROU! É um número MENOR... Tente novamente: '))
    else:
        num_user = int(input('ERROU! É um númerio MAIOR... Tente novamente: '))

print(f'Você acertou na {tentativas} tentativa.')


