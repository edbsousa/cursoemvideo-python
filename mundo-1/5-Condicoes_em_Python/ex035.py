# Exercício 35 – Analisando Triângulo v1.0
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o comprimento da reta 1: '))
b = float(input('Digite o comprimento da reta 2: '))
c = float(input('Digite o comprimento da reta 3: '))

if a + b > c and a + c > b and b + c > a:
    print('\nÉ possível formar um triângulo.')
else:
    print('\nNão é possível formar um triângulo')
