# Exercício Python 53 - Detector de Palíndromo
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# entrada da frase, fazendo split e depois join para unir sem espaçamento. Lower pra evitar erro.
frase_normal = ''.join(str(input('Digite uma frase: ')).split()).lower()
# solução mais simples para obter o nome invertido: "frase_invertida = frase_normal[::-1]".

# usando for, que é a proposta da aula.
frase_invertida = ''
for i in range(len(frase_normal) - 1, - 1, -1):
    frase_invertida += frase_normal[i]

if frase_normal == frase_invertida:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')










