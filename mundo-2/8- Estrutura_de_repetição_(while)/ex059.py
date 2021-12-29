# Exercício Python 59 - Criando um Menu de Opções
# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

valor1 = float(input('\nDigite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

while opcao != 5:
    opcao = int(input(f'\nQual operação deseja fazer com os números {valor1} e {valor2}?'
                      '\n[ 1 ] somar'
                      '\n[ 2 ] multiplicar'
                      '\n[ 3 ] maior'
                      '\n[ 4 ] novos números'
                      '\n[ 5 ] sair do programa'
                      '\n\nEscolha: '))


    while opcao < 1 or opcao > 5:
        opcao = int(input('Opção inválida! Escolha uma opção correta: '))

    if opcao == 4:
        valor1 = float(input('\nDigite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))

    elif opcao == 1:
        print('Você escolheu a opção para somar:')
        print(f'{valor1} + {valor2} = {valor1+valor2}')

    elif opcao == 2:
        print('Você escolheu a opção para multiplicar:')
        print(f'{valor1} x {valor2} = {valor1*valor2}')

    elif opcao == 3:
        print('Você escolheu a opção para mostrar o maior número digitado:')
        if valor1 > valor2:
            print(valor1)
        elif valor1 < valor2:
            print(valor2)
        else:
            print('Números iguais')

print('Você saiu do programa.')

