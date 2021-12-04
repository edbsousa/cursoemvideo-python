# Exercício 22 – Analisador de Textos
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# a. O nome com todas as letras maiúsculas e minúsculas.
# b. Quantas letras integral (sem considerar espaços).
# c. Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: '))

# a. Uso a função de transformação e retiro qualquer espaço das extremidades.
print('\n• Seu nome com as letras:'
      f'\nMaiúsculas: {nome.upper().strip()}'  
      f'\nMinúsculas: {nome.lower().strip()}')

# b. crio uma lista do nome digitado, retiro os espaço e depois faço a junção.
print(f'\n• Seu nome completo contém:\n{len("".join(nome.split()))} letas.')

# c. crio uma lista do nome digitado e exibo o primeiro elemento.
print(f'\n• Seu primeiro nome contém:\n{len(nome.split()[0])} letras.')

