# Exercício Python 73 - Tuplas com Times de Futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = (
'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'América-MG',
'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia',
'Sport', 'Chapecoense')


print('=' * 50)
print(f'{"BRASILEIRÃO 2021 - SÉRIE A":^50}')
print('=' * 50 + '\n')

print('Os primeiros 5 colocados')
for i in range(0, 5):
    print(f'{i + 1} - {tabela[i]}')

print('\nOs últimos 4 colocados')
for i in range(16, 20):
    print(f'{i + 1} - {tabela[i]}')

tabela2 = sorted(tabela)
print('\nParticipantes em ordem alfabetica')
for i in range(0, 20):
    print(f'{tabela2[i]}')

print(f'\nA Chapecoense ficou na {tabela.index("Chapecoense") + 1} posição.')

