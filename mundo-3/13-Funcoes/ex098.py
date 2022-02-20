# Exercício Python 98 - Função de Contador
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end=' ')
            cont += passo
            sleep(0.25)
        print('FIM!')
        print('='*50)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.25)
        print('FIM!')
        print('=' * 50)


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Digite os valores personalizados:')
iniciop = int(input('• Início: '))
fimp = int(input('• Fim: '))
passop = int(input('• Passo: '))
contador(iniciop, fimp, abs(passop))

