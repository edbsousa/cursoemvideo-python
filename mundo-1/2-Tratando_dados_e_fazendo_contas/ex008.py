# Exercício 8 – Conversor de Medidas
# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

msg = "CONVERSOR DE MEDIDAS"
print('='*45 + f'\n{msg:^45}\n' + '='*45)
metros = float(input(f'\nDigite o valor em metros a ser convertido: '))

print(f'\n- O valor {metros}m em centímetros é {metros * 100:.0f}cm')
print(f'- O valor {metros}m em milímetros é {metros * 1000:.0f}mm')
