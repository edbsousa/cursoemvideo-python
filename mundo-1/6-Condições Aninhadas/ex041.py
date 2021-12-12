# Exercício 41 – Classificando Atletas
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

idade = int(input('Digite a sua idade: '))

if idade < 10:
    print(f'A sua categoria é: MIRIM.')
elif idade < 15:
    print(f'A sua categoria é: INFANTIL.')
elif idade < 20:
    print(f'A sua categoria é: JÚNIOR.')
elif idade < 26:
    print(f'A sua categoria é: SÊNIOR.')
else:
    print(f'A sua categoria é: MASTER.')
