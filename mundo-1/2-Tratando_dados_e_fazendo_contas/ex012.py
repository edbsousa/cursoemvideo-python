# Exercício 12 – Calculando Descontos
# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

msg = "PRODUTO COM DESCONTO"
print('='*45 + f'\n{msg:^45}\n' + '='*45)

valor = float(input('Digite o preço do produto: R$'))
valordesconto = valor * 0.95
print(f'Você ganhou 5% de desconto. \nO novo valor a ser pago é: R${valordesconto:.2f}.')
