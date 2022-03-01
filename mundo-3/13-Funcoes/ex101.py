# Exercício Python 101 - Funções para votação
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(anonascimento):
    from datetime import datetime
    idade = datetime.today().year - anonascimento
    if idade < 18:
        return f"NEGADO! Você tem {idade} anos, não é obrigatório votar."
    elif idade >= 18 and idade < 65:
        return f"OBRIGATÓRIO! Você tem {idade} anos, precisa votar."
    else:
        return f"OPCIONAL! Você tem {idade} anos, vote apenas se desejar."


print(voto(int(input('Digite o ano de nascimento: '))))

