# Exercício 37 – Conversor de Bases Numéricas
# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('Digite a opção para a conversão:'
                  '\n1 - Binário.'
                  '\n2 - Octal.'
                  '\n3 - Hexadecimal.')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'\nO número convertido para BINÁRIO é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'\nO número convertido para OCTAL é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'\nO número convertido para HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('\nOpção inválida, tente novamente.')


