# Exercício 10 – Conversor de Moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar. Considere US$1.00 = R$3.27


msg = "COMPRA DE DÓLAR"
print('='*45 + f'\n{msg:^45}\n' + '='*45)
real = float(input('\nDigite a quantia em Reais R$ que você possui: '))

cambio = float(3.27)
dolar = float(real * cambio)

print(f'Você tem R${real:.2f}, portanto você pode comprar US${dolar:.2f}.')

