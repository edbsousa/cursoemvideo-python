# Exercício 27 – Primeiro e último nome de uma pessoa
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).title()
nome = nome.split()[0:1] + nome.split()[-1:]

print(f'\nSeu nome, considerando apenas seu primeiro e último nome:\n'
      f'{" ".join(nome)}')


