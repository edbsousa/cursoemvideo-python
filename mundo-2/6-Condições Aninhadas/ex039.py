# Exercício 39 – Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

nascimento = int(input('Digite o ano de nascimento: '))

idade = datetime.datetime.now().year - nascimento

if idade == 18:
    print('Você precisar se alistar este ano.')
elif idade < 18:
    print(f'Você tem/ou ainda vai fazer no ano corrente {idade} anos. '
          f'\nPortanto, ainda precisará se alistar:'
          f'\nFaltam {18 - idade} anos.')
else:
    print(f'Você tem/ou ainda vai fazer no ano corrente {idade} anos. '
          f'\nPortanto, já ultrapassou da idade de alistamento:'
          f'\nPassou {idade - 18} anos.')
