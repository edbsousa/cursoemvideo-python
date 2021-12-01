# Exercício 18 – Seno, Cosseno e Tangente
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo: '))

print(f'\nO valor do seno é: {sin(radians(angulo)):.2f}. '
      f'\nO valor do cosseno é {cos(radians(angulo)):.2f}. '
      f'\nE o valor da tangente é {tan(radians(angulo)):.2f}.')
