# Exercício 19 – Sorteando um item na lista
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

name1 = str(input(f'Digite o primeiro nome: '))
name2 = str(input('Digite o segundo nome: '))
name3 = str(input('Digite o terceiro nome: '))
name4 = str(input('Digite o quarto nome: '))

lista = [name1, name2, name3, name4]

print(f'O aluno escolhido foi: {choice(lista)}.')
