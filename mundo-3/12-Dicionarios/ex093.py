# Exercício Python 93 - Cadastro de Jogador de Futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
qtdPartidas = []
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite a quantidade de partidas realizadas: '))
for i in range(0, partidas):
    qtdPartidas.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['gols'] = qtdPartidas
jogador['totalGols'] = sum(qtdPartidas)
print('=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('=' * 40)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas:")
for c, i in enumerate(jogador['gols']):
    print(f'=> Na partida {c+1}, fez {i} gols.')
print('=' * 40)

