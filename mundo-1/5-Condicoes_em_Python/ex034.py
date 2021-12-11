# Exercício 34 – Aumentos múltiplos.
# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

salario = float(input('Digite o seu salário: R$ '))

if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.1

print(f'Você terá {aumento / salario - 1:.0%} de aumento e seu novo salário será: R${aumento:.2f}')



