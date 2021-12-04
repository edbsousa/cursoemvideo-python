# Exercício 23 – Separando dígitos de um número
# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um númeno entre 0 a 9999: '))

print(f'\n • Unidade: {num % 10}'
      f'\n • Dezena: {(num % 100) // 10}'
      f'\n • Centena: {(num % 1000) // 100}'
      f'\n • Milhar: {num // 1000}')


