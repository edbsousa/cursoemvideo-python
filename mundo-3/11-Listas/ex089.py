# Exercício Python #089 - Boletim com listas compostas
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

# alunos = [['Edeilson', [5.5, 7.8]], ['Aline', [6.3, 4.5]], ['Priscila', [9.8, 8.1]]]

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Deseja constinuar? Digite qualquer tecla para continuar ou "n" para interromper. '))
    if opcao in 'Nn':
        break
print()
print('==' * 25)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opcao = int(input('Deseja mostrar notas de qual aluno? (999 para interromper):'))
    if opcao == 999:
        print('FIM!', end=' ')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}.')
print('VOLTE SEMPRE.')
