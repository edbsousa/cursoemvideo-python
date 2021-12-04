# Exercício 24 – Verificando as primeiras letras de um texto
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome da cidade em que nasceu: ')).title().split()
santo = "Santo" in cidade[0]
print(santo)
