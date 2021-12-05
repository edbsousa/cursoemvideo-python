# Exercício 29 – Radar eletrônico
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint

print('\n' + '\33[1m=-=-= RADAR - LIMITE 80Km/h =-=-=\33[m')
velocidade = randint(70, 90)
print(f'\n • Velocidade do seu carro {velocidade}Km/h.\n')

if velocidade <= 80:
    print(f'\033[32m • Você está dentro da velocidade permitida de 80Km/h.')
else:
    print(f'\033[31m • ACIMA DA VELOCIDADE!!! Ultrapassou {velocidade - 80}Km/h.\n'
          f' • Você será multado em \33[1mR${(velocidade - 80) * 7:.2f}.')



