# Exercício Python 82 - Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = list()
par = list()
impar = list()
while True:
    numeros.append(int(input('Digite o número: ')))
    while True:
        opcao = str(input('Deseja continuar [S/N]?: '))
        if opcao in 'NnSs':
            break
        else:
            print('Tente novamente!', end=' ')
    if opcao in 'Nn':
        break
print('===' * 30)
print(f'Os números digitados: {numeros}')
for valor in numeros:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')

