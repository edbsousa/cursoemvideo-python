# Exercício 43 – Índice de Massa Corporal
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso (ex.: 69.2): '))
altura = float(input('Digite sua altura (ex.: 1.70): '))
imc = peso / (altura * altura)

print(f'Seu IMC: {imc:.2f}')

if imc < 18.5:
    print(f'Classificação: Abaixo do Peso')
elif 18.5 <= imc < 25:
    print(f'Classificação: Peso Ideal')
elif 25 <= imc < 30:
    print(f'Classificação: Sobrepeso')
elif 30 <= imc < 40:
    print(f'Classificação: Obesidade')
else:
    print(f'Classificação: Obesidade Mórbida')


