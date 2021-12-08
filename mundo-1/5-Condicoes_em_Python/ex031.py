# Exercício 31 – Custo da Viagem
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 parta viagens mais longas.

distancia_km = float(input('Digite a distância da viagem em Km: '))

if distancia_km < 200.00:
    print(f'O preço a pagar é de R${distancia_km * 0.50:.2f}')
else:
    print(f'O preço a pagar é de R${distancia_km * 0.45:.2f}')
