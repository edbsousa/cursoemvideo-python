# Exercício 33 – Maior e menor valores
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

menor = num1
if num2 < num1 and num2:
    menor = num2
if num3 < num1 and num2:
    menor = num3

maior = num1
if num2 > num1 and num3:
    maior = num2
if num3 > num1 and num2:
    maior = num3

print(f'\nO menor número digitado foi o {menor}')
print(f'O maior número digitado foi o {maior}')




