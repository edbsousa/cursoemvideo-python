# Aprovando Empréstimo
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
qtd_anos = int(input('Digite em quantos anos deseja pagar: '))
salario = float(input('Digite seu salário: '))

valor_parcela = valor_casa / (qtd_anos * 12)  # 80000 / (7 * 12)
limite = 0.3 * salario
excede = valor_parcela - limite

if valor_parcela > limite:
    print(f'\nEMPRÉSTIMO NEGADO!')
    print(f'O valor mensal a ser pago ultrapassou 30% do seu salário.'
          f'\nSeu salário: {salario}'
          f'\nValor da parcela: {valor_parcela:.2f} '
          f'\nExcedeu {excede:.2f}')
else:
    print(f'\nEMPRÉSTIMO AUTORIZADO')
    print(f'Você irá pagar R${valor_parcela} mensalmente por {qtd_anos} anos')

