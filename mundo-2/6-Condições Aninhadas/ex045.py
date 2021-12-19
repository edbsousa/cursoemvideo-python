# Exercício 45 – GAME: Pedra Papel e Tesoura

from random import choice
from time import sleep

opcoes = 'pedra papel tesoura'.split()

pc = choice(opcoes)

print("====== JOKENPÔ ======\n"
      "Pedra, papel e tesoura")
usuario = str(input('DIGITE a sua opção: ')).lower()

print(f'\nJO ', end='')
sleep(0.5)
print(f'KEN ', end='')
sleep(0.5)
print(f'PÔ \n', end='')
sleep(0.5)

if pc == usuario:
    print('Empate! Jogue novamente.')

elif pc == 'pedra' and usuario == "tesoura":
    print('PERDEU! O PC ESCOLHEU PEDRA :( \nO computador quebrou sua tesoura!')

elif pc == 'tesoura' and usuario == "pedra":
    print('GANHOU! O PC ESCOLHEU TESOURA :) \nVocê quebrou a tesoura do computador.')

elif pc == 'tesoura' and usuario == "papel":
    print('PERDEU! O PC ESCOLHEU TESOURA :( \nO computador cortou seu papel!')

elif pc == 'papel' and usuario == "tesoura":
    print('GANHOU! O PC ESCOLHEU PAPEL :) \nVocê cortou o papel do computador.')

elif pc == 'papel' and usuario == "pedra":
    print('PERDEU! O PC ESCOLHEU PAPEL :( \nO computador embrulhou sua pedra!')

elif pc == 'pedra' and usuario == "papel":
    print('GANHOU! O PC ESCOLHEU PEDRA :) \nVocê embrulhou a pedra do computador.')



