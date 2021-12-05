# Exercício 28 – Jogo da Adivinhação v.1.0
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep
from pygame import mixer, init

num = randrange(0, 5, 1)

print('\n')
print('=-=' * 20)
num_user = int(input('O computador “pensou” em um número inteiro entre 0 e 5.'
                     '\nTente adivinhar: '))

print('\nPROCESSANDO...')

mixer.init()
init()
mixer.music.load('ex028-dramatic-hit.mp3')
mixer.music.play(loops=0, start=0.0)

sleep(5)

if num_user == num:
    print('\nPARABÉNS! Você acertou.')
    print(f'O computador "pensou" no número {num}.')
    mixer.init()
    init()
    mixer.music.load('ex028-right-ring-.mp3')
    mixer.music.play(loops=0, start=0.0)
    sleep(5)
else:
    print('\nNÃO FOI DESSA VEZ! Você errou.')
    print(f'O computador "pensou" no número {num}.')
    mixer.init()
    init()
    mixer.music.load('ex028-fail-ring.mp3')
    mixer.music.play(loops=0, start=0.0)
    sleep(3)


