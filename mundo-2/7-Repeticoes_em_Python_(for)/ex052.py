# Exercício Python 52 - Números primos
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

primo = 0
for i in range(1, num + 1, 1):
    if num % i == 0:
        print(f'\033[32m {i} \33[m', end=' ')
        primo += 1
    else:
        print(f'\033[31m {i} \33[m', end=' ')
if primo == 2:
    print('\nNúmero primo.\n'
          f'O número {num} foi divisível {primo} vezes.')
else:
    print('\nNão é primo.\n'
          f'O número {num} foi divisível {primo} vezes.')

