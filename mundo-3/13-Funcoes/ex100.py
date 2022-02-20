# Exercício Python #100 - Funções para sortear e somar
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia():
    numeros = list()
    for i in range(0, 5):
        numeros.append(randint(0, 20))
    return numeros


def somapar():
    soma_par = 0
    num_sorteio = sorteia()
    for i in num_sorteio:
        if i % 2 == 0:
            soma_par += i
    print(f'Sorteando os números...', end=' ')
    sleep(1)
    for i in num_sorteio:
        print(i, end=' ')
        sleep(0.5)
    print(f'\nA soma dos números pares é {soma_par}.')


somapar()
