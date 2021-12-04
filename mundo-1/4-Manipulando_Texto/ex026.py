# Exercício 26 – Primeira e última ocorrência de uma string
# Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

frase = str(input('Digite sua frase: ')).strip().lower()

print(f'\nA letra "A" aparece {(frase.count("a"))} frase digitada.')
print(f'A primeira vez que a letra "A" aparece é na posição {(frase.find("a"))+1}.')
print(f'A última vez que a letra "A" aparece é na posição {(frase.rfind("a"))+1}.')


