# Exercício 6 – Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número para obter o dobro, triplo e raiz quadrada: '))

dobro = num * 2
triplo = num * 3
raizq = num**(1/2)


print(f'\n- O dobro de {num} é {dobro}.')
print(f'- O triplo de {num} é {triplo}.')
print(f'- E a raiz quadrada de {num} é {raizq:.2f}')

