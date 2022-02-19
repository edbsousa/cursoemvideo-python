# Exercício Python 92 - Cadastro de Trabalhador em Python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

cadastro = dict()
cadastro['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite o ano de nascimento (4 dígitos): '))
cadastro['idade'] = datetime.today().year - nascimento
while True:
    carteira = int(input('Digite o nº de sua CTPS (caso não tenha, digite 0): '))
    if carteira == 0:
        break
    else:
        cadastro['carteira'] = carteira
        contrat = int(input('Digite o ano da contratação: '))
        cadastro['ano_contratacao'] = contrat
        cadastro['salario'] = float(input('Digite o salário: '))
        cadastro['aposentadoria'] = (datetime.today().year - nascimento) + (contrat + 35 - datetime.today().year)
        break

for k, v in cadastro.items():
    print(f'{k} - {v}')




