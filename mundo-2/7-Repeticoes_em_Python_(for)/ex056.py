# Exercício Python #056 - Analisador completo
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

h_velho = 0
h_velho_nome = ''
mulheres = 0
media = 0
soma_idade = 0

for i in range(1, 5, 1):
    print(f'\n======== {i} pessoa ========')
    nome = str(input('Digite o nome: ')).title()
    idade = int(input(f'Digite a idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).lower()

    soma_idade += idade
    media = soma_idade / i

    if sexo == 'm':
        if idade > h_velho:
            h_velho = idade
            h_velho_nome = nome
    elif sexo == 'f' and idade < 20:
        mulheres += 1


if h_velho_nome == '':
    print('• Não consta nenhum nome masculino na listagem.')
else:
    print(f'\n• O nome do homem mais velho digitado foi {h_velho_nome}, que tem {h_velho} anos.')

if mulheres == 0:
    print('• Não consta nenhum nome feminino na listagem.')
elif mulheres == 1:
    print('• Foi digitado 1 nome de mulher.')
else:
    print(f'• Foi digitado {mulheres} nomes de mulheres.')

print(f'• A média de idade do grupo é de {media:.2f}.')

