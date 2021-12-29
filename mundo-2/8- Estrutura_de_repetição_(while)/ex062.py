# Exercício Python 62 - Super Progressão Aritmética v3.0
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = 0
while razao == 0:
    razao = int(input('Digite a razão da PA: '))
decimo = primeiro_termo + (10 - 1) * razao

i = primeiro_termo
while i <= decimo:
    print(i, end=' -> ')
    i += razao
print('PAUSA\n')

i2 = i

maistermo = -1
contagem = 10
while maistermo != 0:
    maistermo = int(input('Digite mais quantos termos deseja visualizar (ou 0 para sair): '))
    contagem += maistermo
    if maistermo != 0:
        maistermo = i2 + (maistermo - 1) * razao
        while i <= maistermo:
            print(i, end=' -> ')
            i += razao
        print('PAUSA\n')
        i2 = i
    else:
        maistermo = 0
print(f'Progressão finalizada com {contagem} termos mostrados.')




