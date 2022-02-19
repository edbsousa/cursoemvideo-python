# Exercício Python 95 - Aprimorando os Dicionários
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
jogadores = []

while True:
    qtdPartidas = []
    somagols = 0
    print('-' * 40)
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Digite a quantidade de partidas realizadas: '))
    for i in range(0, partidas):
        qtdPartidas.append(int(input(f'Quantos gols na partida {i+1}? ')))
    for gols in qtdPartidas:
        somagols += gols
    jogador['gols'] = qtdPartidas
    jogador['totalGols'] = somagols
    jogadores.append(jogador.copy())

    opcao = str(input('Deseja cadastrar outro jogador? [s/n]: '))
    if opcao in 'Nn':
        break
print('=' * 50)

print(jogadores)
print('='*62)
print(f"{'Índice':<10}  {'Nome':<15}  {'Gols':<15} {'Total Gols':>15}.")
for e, i in enumerate(jogadores):
    print(f"{e:<10}  {i['nome']:<15}  {i['gols']!s:<15s} {i['totalGols']:>15}")
print('='*62)

while True:
    while True:
        dados_jogador = int(input('Mostrar dados de qual jogador? '
                                  '\nDigite o índice ou 999 para sair: '))
        if dados_jogador <= len(jogadores) or dados_jogador < 0 or dados_jogador == 999:
            break
        else:
            print('ÍNDICE INVÁLIDO!', end=' ')
    if dados_jogador == 999:
        break
    print(f"• Levantamento do jogador: {jogadores[dados_jogador]['nome']}.")
    for e, i in enumerate(jogadores):
        if e == dados_jogador:
            for ee, j in enumerate((i['gols'])):
                print(f"- Na {ee}º partida, fez {j} gols.")
    print('-'*50)
print('FIM!')
