# Exercício Python 102 - Função para Fatorial
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    :param num: informar o número que deseja realizar o fatorial
    :param show: (opcional) se True, mostra o conta além do resultado.
    :return: mostra o resultado do fatorial.
    Código criado por Edeilson Sousa.
    """
    if show:
        for c in range(num, 0, -1):
            if c == 1:
                print('1 = ', end='')
            else:
                print(c, end=' x ')
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


numerofat = int(input("Digite o número para o fatorial: "))
print(fatorial(numerofat, show=True))
