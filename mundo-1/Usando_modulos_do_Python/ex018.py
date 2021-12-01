# Exercício 18 – Seno, Cosseno e Tangente
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan

angulo = int(input('Digite o ângulo: '))

print(f'\nO valor do seno é: {sin(angulo)}. '
      f'\nO valor do cosseno é {cos(angulo)}. '
      f'\nE o valor da tangente é {tan(angulo)}.')
