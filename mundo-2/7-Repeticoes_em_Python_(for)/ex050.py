# Exercício Python 50 - Soma dos pares
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for i in range(0, 6, 1):
    num = int(input(f'Digite o {i + 1}º número: '))
    if num % 2 == 0:
        soma += num

print(f'\nA soma apenas dos números pares é {soma}.')


