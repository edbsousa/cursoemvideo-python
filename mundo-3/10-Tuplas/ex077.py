# Exercício Python 77 - Contando vogais em Tupla
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). D
# epois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tabela = ('Palmeiras', 'Corinthians', 'Red Bull Bragantino', 'Santos', 'Sao Paulo')

for i in tabela:
    print(f'\nNo nome do time {i.upper()} temos as vogais', end=' ')
    for letra in i:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')







