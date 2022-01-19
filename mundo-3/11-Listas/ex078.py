# Exercício Python 78 - Maior e Menor valores na Lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {i}: ')))
maior = menor = valores[0]
for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print(f'\nO maior valor digitado foi {maior} na posição/posições:', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i} - ', end='')
print()
print(f'E o menor foi {menor} na posição/posições:', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i} - ', end='')
print()
