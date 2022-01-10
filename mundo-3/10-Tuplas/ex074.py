# Exercício Python 74 - Maior e menor valores em Tupla
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))

print('Os números sorteados foram: ', end='')
for i in range(0, 5):
    print(numeros[i], end=" ")

# maior = numeros[0]
# menor = numeros[0]
# for i in range(1, 5):
#     if numeros[i] > maior:
#         maior = numeros[i]
#     if numeros[i] < menor:
#         menor = numeros[i]

print(f'\nO maior número sorteado foi o {max(numeros)}.')
print(f'E o menor foi {min(numeros)}.')



