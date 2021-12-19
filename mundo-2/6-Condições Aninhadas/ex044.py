# Exercício 44 – Gerenciador de Pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Digite o valor do produto: '))
print('Veja as opções de pagamento disponíveis: '
      '\n1 - à vista dinheiro/cheque: 10% de desconto'
      '\n2 - à vista no cartão: 5% de desconto'
      '\n3 - em até 2x no cartão: preço formal'
      '\n4 - 3x ou mais no cartão: 20% de juros')

opcao_pagamento = int(input('\nDigite a opção de como deseja pagar: '))

if opcao_pagamento == 1:
    print(f'Você escolheu a opção 1.'
          f'\nVai obter 10% de desconto. O novo valor a ser pago à vista dinheiro/cheque:'
          f'\nR${valor_produto * 0.9:.2f}')

elif opcao_pagamento == 2:
    print(f'Você escolheu a opção 2.'
          f'\nVai obter 5% de desconto. O novo valor a ser pago à vista no cartão:'
          f'\nR${valor_produto * 0.95:.2f}')

elif opcao_pagamento == 3:
    parcela = int(input('Você escolheu a opção 3.'
                        '\n\nDeseja pagar em 1 ou 2 parcelas?'
                        '\nEscolha a opção: '))
    if parcela == 1:
        print(f'\nA vista no cartão:'
              f'\nR${valor_produto:.2f}')
    elif parcela == 2:
        print(f'\nEm 2 parcelas no cartão:'
              f'\nParcela 1: R${(valor_produto / 2):.2f}'
              f'\nParcela 2: R${(valor_produto / 2):.2f}')

elif opcao_pagamento == 4:
    parcela = int(input('Você escolheu a opção 4.'
                        '\n\nDeseja pagar em quantas parcelas?'
                        '\nEscolha a opção: '))
    print(f'\nVocê irá pagar em {parcela} vezes.'
          f'\nR${((valor_produto / parcela) * 1.2):.2f} o valor de cada parcela.')
else:
    print('OPÇÃO INVÁLIDA! DIGITE UMA DAS OPÇÕES DISPONÍVEIS.')
