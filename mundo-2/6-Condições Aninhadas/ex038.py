# Exercício 38 – Comparando números
# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro valor digitado é o maior.')
elif num2 > num1:
    print('O segundo valor digitado é o maior.')
else:
    print(f'Os números digitados são iguais.')


