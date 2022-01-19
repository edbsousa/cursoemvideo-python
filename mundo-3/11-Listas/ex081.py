# Exercício Python 81 - Extraindo dados de uma Lista
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
while True:
    valores.append(int(input('Digite o número: ')))
    while True:
        opcao = str(input('Deseja continuar [S/N]: '))
        if opcao in 'NnSs':
            break
        else:
            print('Tente novamente!', end=' ')
    if opcao in 'Nn':
        break
print()
print(f'Foram digitados {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os números digitados em ordem decrescente: {valores}')
if 5 in valores:
    print('O número cinco foi digitado.')
else:
    print('O número 5 não foi digitado.')
