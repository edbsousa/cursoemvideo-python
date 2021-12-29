# Exercício Python 63 - Sequência de Fibonacci v1.0
# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('=== SEQUÊNCIA DE FIBONACCI ===')
termo = int(input('Quantos termos deseja mostras? Digite: '))

i = 3
antecessor = 1
sucessor = 1
soma = 0

print('0  ->  1', end='  ->  ')
while i <= termo:
    soma = antecessor + sucessor
    antecessor = sucessor
    sucessor = soma
    print(antecessor, end='  ->  ')
    i += 1
print('FIM')
