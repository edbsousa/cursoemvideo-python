# Exercício Python 80 - Lista ordenada sem repetições
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista_num = list()
for i in range(0, 5):
    num = int(input('Digite o número: '))
    if i == 0 or num > lista_num[-1]:
        lista_num.append(num)
        print('Adicionado no fim da lista.')
    else:
        posicao = 0
        while posicao < len(lista_num):
            if num <= lista_num[posicao]:
                lista_num.insert(posicao, num)
                print(f'Adicionado na posição {posicao}.')
                break
            posicao += 1
print(f'Os valores digitados foram {lista_num}')


