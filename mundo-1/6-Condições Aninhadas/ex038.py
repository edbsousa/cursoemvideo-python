# Exercício 38 – Comparando números
# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num2 < num1:
    print(f'O menor número digitado foi o {num2}.')
elif num1 == num2:
    print('Os números são iguais.')
else:
    print(f'O menor número digitado foi o {num1}')


