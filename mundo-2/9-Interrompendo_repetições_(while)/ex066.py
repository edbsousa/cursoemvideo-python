# Exercício Python 66 - Vários números com flag
# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = i = 0

while True:
    num = int(input('Digite o número: '))
    if num == 999:
        break
    i += 1
    soma += num

print(f'''\nForam digitados {i} números.
A soma dos valores digitados é {soma}.''')
