# Exercício Python 57 - Validação de Dados
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' != 'F':
    sexo = str(input('Escolha o seu sexo [F/M]: ')).upper()
    if sexo != 'M' != 'F':
        print(f'A opção {sexo} não á válida. \nTente novamente!', end=' ')

print('Pronto! Informação recebida.')
