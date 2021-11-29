# Exercício 13 – Reajuste Salarial
# Faça um algoritmo que leia o salário de um funcionário
# e mostre o seu novo salário com 15% de aumento

salario = float(input('Digite seu salário atual: R$'))
aumento = 1.15  # aumento de 15% em decimais
print(f'Conforme informe, você terá {aumento - 1:.0%} de aumento, '
      f'portanto seu novo salário será de R$ {salario * aumento:.2f}.')
