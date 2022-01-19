# Exercício Python 79 - Valores únicos em uma Lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()
opcao = ' '
while opcao not in 'N':
    valor = int(input('Digite o valor: '))
    if valor in valores:
        valor = int(input('Valor já digitado! Digite outro valor: '))
    valores.append(valor)
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while opcao not in 'NS':
        opcao = str(input('Valor inválido!! Deseja continuar? [S/N] ')).strip().upper()
print(f'Foram digitados os valores: {sorted(valores)}')


