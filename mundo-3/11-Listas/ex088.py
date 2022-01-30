# Exercício Python 88 - Palpites para a Mega Sena
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos = []
jogo = []
q = 0
print('-$-' * 10)
print(f'{"GERADOR JOGO MEGA SENA":^30}')
print('-$-' * 10)
print()
qtdjogos = int(input('Quantos jogos deseja gerar? Responda: '))

while q < qtdjogos:
    for i in range(0, 6):
        while True:
            num = randint(0, 60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    q += 1

for i in range(0, len(jogos)):
    sleep(1)
    print(f'Jogo {i+1}:', end=' ')
    for j in range(0, 6):
        print(jogos[i][j], end=' ')
    print()
print()
sleep(1)
print('-=-' * 10)
print(f'{"BOA SORTE!":^30}')
print('-=-' * 10)
