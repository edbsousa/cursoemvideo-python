# Exercício Python 61 - Progressão Aritmética v2.0
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro_termo + (10 - 1) * razao

i = primeiro_termo
while i <= decimo:
    print(i, end=' -> ')
    i += razao
print('FIM')
