# Exercício Python 99 - Função que descobre o maior
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
from random import randint


def loading():
    for i in range(0, 3):
        sleep(0.5)
        print('.', end='')
    print()
    sleep(0.5)


def maior(* numeros):
    print('='*60)
    print('Analisando os números informados', end='')
    loading()
    m = 0
    for i, n in enumerate(numeros):
        if i == 0:
            m = n
        if n > m:
            m = n
    print(f'Foram informados {len(numeros)} números:', end=' ')
    for i, n in enumerate(numeros):
        print(n, end='')
        if i < len(numeros)-2:
            print(', ', end='')
        elif i == len(numeros)-2:
            print(' e ', end='')
    print('.')
    sleep(1)
    print(f'E o maior digitado foi o {m}.')
    print('=' * 60)


maior(1, 2, 100, 4, 5, 50)
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior()
