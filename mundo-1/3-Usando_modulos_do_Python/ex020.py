# Exercício 20 – Sorteando uma ordem na lista
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

name1 = str(input('Digite o primeiro nome: '))
name2 = str(input('Digite o segundo nome: '))
name3 = str(input('Digite o terceiro nome: '))
name4 = str(input('Digite o quarto nome: '))

lista = [name1, name2, name3, name4]
random.shuffle(lista)

print(lista)
