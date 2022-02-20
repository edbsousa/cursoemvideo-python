# Exercício Python 96 - Função que calcula área
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(b, a):
    print(f'A área de um terreno {b} x {a} é {base * altura}m².')


def titulo():
    print('-'*30)
    print(f'{"ÁREA DO TERRENO":^30}')
    print('-'*30)


# programa principal
titulo()
base = float(input('Digite a base (m): '))
altura = float(input('Digite a largura/altura (m): '))

area(base, altura)


