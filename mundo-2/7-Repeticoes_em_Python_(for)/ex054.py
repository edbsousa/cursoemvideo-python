# Exercício Python 54 - Grupo da Maioridade
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
for i in range(1, 8, 1):
    nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = date.today().year - nascimento
    if idade >= 18:
        maior += 1

if maior == 6:
    print(f'\nTem {maior} pessoas que já são de maiores.\n'
          f'E apenas {7 - maior} pessoa ainda não atingiu a maioridade.')
elif maior == 1:
    print(f'\nTem apenas {maior} pessoa que já é de maior.\n'
          f'E {7 - maior} não atingiram a maioridade.')
else:
    print(f'\nTem {maior} pessoas que já são de maiores.\n'
          f'E {7 - maior} não atingiram a maioridade.')
