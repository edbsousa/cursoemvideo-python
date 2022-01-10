# Exercício Python 76 - Lista de Preços com Tupla
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produto_preco = ('Açúcar Refinado União Pacote 1kg', 4.28,
                 'Feijão Carioca Tipo 1 Camil Pacote 1 Kg', 7.98,
                 'Óleo De Soja Liza Pet 900mL', 8.48,
                 'Arroz Tipo1 Camil 5kg', 21.80,
                 'Sal Cisne Tradicional 1kg', 2.98)


print('='*60 + f'\n{"PRODUTOS BÁSICOS - PREÇOS":^45}\n' + '='*60)

for i in range(0, len(produto_preco), 2):
    print(f'{produto_preco[i]:.<50}R$ {produto_preco[i + 1]:>7.2f}')
print('='*60)




