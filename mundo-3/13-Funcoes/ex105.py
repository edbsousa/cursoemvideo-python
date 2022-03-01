# Exercício Python 105 - Analisando e gerando Dicionários
#  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
#  vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(* r, sit=False):
    """
    :param r: Aceita inumeras notas de vários alunos.
    :param sit: entrada opcional, definindo se deve mostrar a situação ou não.
    :return: retorna um dicionário com as informações da turma
    """
    infos = dict()
    maior = menor = soma = 0
    for c, i in enumerate(r):
        soma += i
        if c == 0:
            maior = i
            menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
    infos['menor'] = menor
    infos['maior'] = maior
    infos['media'] = soma / len(r)
    if sit:
        if infos['media'] <= 4:
            infos['situacao'] = 'RUIM!'
        if 5 <= infos['media'] <= 7:
            infos['situacao'] = 'RAZOAVEL!'
        if infos['media'] > 7:
            infos['situacao'] = 'BOA!'
    return infos


print(notas(5.7, 6.2, 7.1, 6.5, sit=True))
