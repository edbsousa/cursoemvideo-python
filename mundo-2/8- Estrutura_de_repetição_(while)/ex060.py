# Exercício Python 060 - Cálculo do Fatorial
# Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número natural: '))

print(f'O fatorial de {num}! é:')  # 5

print('\nUsando o WHILE:')
i = num
f = 1
while i > 1:
    print(i, end=' x ')
    f *= i
    i = i - 1
print(f'1 = {f}')


print('\nUsando o FOR:')
i = num
f2 = 1
for i in range(num, 1, -1):
    print(i, end=' x ')
    f2 *= i
print(f'1 = {f2}')


