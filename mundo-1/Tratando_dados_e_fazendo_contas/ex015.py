# Exercício 15 – Aluguel de Carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite quantos Km você percorreu com o carro: '))
dias = int(input('E agora digite a quantidade de dias que permaneceu com o carro: '))

custo_dia = dias * 60
custo_km = km * 0.15

print(f'\nO total a pagar é de R${custo_km + custo_dia:.2f}')
