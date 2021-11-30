# Exercício 11 – Pintando Parede
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m^2.

msg = "LITROS NECESSÁRIO PARA A PINTURA"
print('='*45 + f'\n{msg:^45}\n' + '='*45)

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print(f'\nA área da sua parede é {area:.2f}m².')
print(f'Portanto, será necessário {area/2:.2f} litros de tinta para pintá-la.')
