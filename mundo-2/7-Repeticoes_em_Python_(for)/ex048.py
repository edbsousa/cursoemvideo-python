# Exercício Python 48 - Soma ímpares múltiplos de três
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print(f'\nA soma dos {cont} números ímpares múltiplos de três entre 1 a 500 é: {soma:.2f}')
