n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media > 7:
    print('Média do aluno é {:.2f}'.format(media))
    print('O aluno está APROVADO!')
elif 7 >= media >= 5:
    print('Média do aluno é {:.2f}'.format(media))
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('Média do aluno é {:.2f}'.format(media))
    print('O aluno está REPROVADO!')
