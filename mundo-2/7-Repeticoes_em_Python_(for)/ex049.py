# Exercício Python 49 - Tabuada v.2.0
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

msg = "TABUADA"
print('='*45 + f'\n{msg:^45}\n' + '='*45)
num = int(input(f'\nDigite um valor inteiro para mostrar a tabuada: '))

for i in range(1, 11, 1):
    print(f'{num} x {i} = {num * i}')
