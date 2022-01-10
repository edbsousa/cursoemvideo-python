# Exercício Python 72 - Número por Extenso
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num_text = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

opcao = ' '
while opcao != 'n':

    while True:
        num_user = int(input('Digite um número entre 0 e 20: '))
        if num_user < 0 or num_user > 20:
            print('Tente novamente!', end=' ')
        else:
            break
    print(f'Você digitou o número {num_text[num_user]}.')

    while True:
        opcao = input('Deseja continuar? [S/N] ').strip().lower()
        if opcao == 's' or opcao == 'n':
            break
