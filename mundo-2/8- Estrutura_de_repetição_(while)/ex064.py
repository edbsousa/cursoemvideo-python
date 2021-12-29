# Exercício Python 64 - Tratando vários valores v1.0
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = i = 0
num = int(input('Digite um número (ou "999" para parar): '))
while num != 999:
    i += 1
    soma += num
    num = int(input('Digite um número (ou "999" para parar): '))
print('FIM\n')
print(f'Foram digitados {i} números e a soma entre os valores é {soma}.')
