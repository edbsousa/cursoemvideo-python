# Exercício Python 65 - Maior e Menor valores
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

opcao = 's'
i = 0
menor = maior = total = anterior = num = 0
while opcao == 's':

    anterior = num

    num = int(input(f'Digite o {i + 1}º número: '))
    opcao = str(input(f'Quer continuar e digitar o {i + 1}º número? '
                      f'\nDigite "s" para continuar ou qualquer outra letra para interromper: ')).lower()

    total += num

    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    print('\n')
    i += 1

print('=' * 70)
print(f'• Soma de todos os números digitados: {total}')
print(f'• Você digitou {i}x. Portanto, a média dos números digitados é: {total / i:.2f}')
print(f'• O maior número digitado foi: {maior}. E o menor foi: {menor}.')
print('=' * 70)
