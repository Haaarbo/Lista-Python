def notas(*n, s=False):
    """
    =>A função notas() é uma função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos(aceita várias)
    :param s: opcional, define a situação do aluno
    :return: dicionário com várias informações sobre a situação da turma.
    """
    #definição dos elementos do dicionario a ser retornado
    d = {'qtd': len(n),
         'maior': max(n),
         'menor': min(n),
         'media': sum(n)/len(n)
         }
    
    #se for requerido que a situação seja exibida
    if s:
        if d['media'] >= 7:
            d['situacao'] = 'BOA'
        elif d['media'] >= 5:
            d['situacao'] = 'RAZOÁVEL'
        else:
            d['situacao'] = 'RUIM'

    #retorno do dicionário
    return d


#Programa principal
r = notas(1, 2, 3, 9,0)
print(r)
help(notas)
