# Exercício Python 75 - Análise de dados em uma Tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


numeros = (
    int(input('Digite o número: ')), int(input('Digite o número: ')),
    int(input('Digite o número: ')), int(input('Digite o número: '))
)

print(f'\nFoi digitado {numeros.count(9)}x o número nove.')
if 3 in numeros:
    print(f'A primeira vez que o nº 3 foi digitado foi na posição {numeros.index(3)+1}.')
else:
    print('O valor três não foi digitado.')
print('Os valores pares digitados foi/foram:', end=' ')
for i in range(0, 4):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=' ')









