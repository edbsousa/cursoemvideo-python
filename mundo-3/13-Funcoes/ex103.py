# Exercício Python 103 - Ficha do Jogador
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado

def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s).')


nome = str(input('Digite o nome: '))
gols = input('Digite a qtd de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)

