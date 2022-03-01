# Exercício Python 106 - Sistema interativo de ajuda em Python
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
# o programa se encerrará. Importante: use cores.
c = ()


def m1():
    msg1 = 'SISTEMA DE AJUDA PyHELP'
    print(f'\033[30;43m', end='')
    print('~' * len(msg1))
    print(msg1)
    print('~' * len(msg1))
    print(f'\033[m')


def m2(ent):
    from time import sleep
    msg2 = f'Acessando o manual do comando {ent}'
    print(f'\033[30;45m', end='')
    print('~' * len(msg2))
    print(msg2)
    print('~' * len(msg2))
    print(f'\033[m')
    sleep(2)


def ajuda(ent):
    print(f'\033[40;7m', end='')
    help(ent)
    print(f'\033[m')


while True:
    m1()
    opcao = str(input('Função ou biblioteca: '))
    if opcao.strip().upper() == 'FIM':
        break
    m2(opcao)
    ajuda(opcao)
print(f'PROGRAMA ENCERRADO!')
