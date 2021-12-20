# Exercício Python 55 - Maior e menor da sequência
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for i in range(1, 6, 1):
    peso = float(input(f'Digite o peso em KG da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso: {maior:.2f}Kg')
print(f'Menor peso: {menor:.2f}Kg')
