# Exercício 17 – Catetos e Hipotenusa
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

print('=== Vamos calcular o comprimento da hipotenusa de um triângulo retângulo ===')
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))

print(f'O comprimento da hipotenusa é {math.hypot(oposto, adjacente):.5f}.')
