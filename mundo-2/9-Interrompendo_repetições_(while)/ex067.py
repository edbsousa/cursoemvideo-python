# Exercício Python 67 - Tabuada v3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:

    valor = int(input('''\nDeseja fazer a tabuada de qual valor? 
(Se valor negativo, programa será encerrado) Digite o nº: '''))

    if valor < 0:
        break

    for i in range(1, 11, 1):
        print(f'{valor} x {i}', end='')
        print('  = ' if i < 10 else ' = ', end='')
        print(valor*i)

print('PROGRAMA FINALIZADO! Volte sempre!!')
