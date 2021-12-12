# Exercício 42 – Analisando Triângulos v2.0
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# Exercício 35 – Analisando Triângulo v1.0
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o comprimento da reta 1: '))
b = float(input('Digite o comprimento da reta 2: '))
c = float(input('Digite o comprimento da reta 3: '))

if a + b > c and a + c > b and b + c > a:
    print('\nÉ possível formar um triângulo:')
    if a == b and c == b:
        print('EQUILÁTERO: todos os lados iguais')
    elif a == b or a == c or b == c:
        print('ISÓSCELES: dois lados iguais, um diferente')
    else:
        print('ESCALENO: todos os lados diferentes')
else:
    print('\nNão é possível formar um triângulo')
