from datetime import date

anoAtual = date.today().year
nascimento = int(input('Insira o ano de nascimento do atleta: '))
idade = anoAtual - nascimento

print('O atleta possui {} anos.'.format(idade))

if idade <= 9:
    categoria = 'MIRIM'
elif 14 >= idade > 9:
    categoria = 'INFANTIL'
elif 19 >= idade > 14:
    categoria = 'JÚNIOR'
elif 25 >= idade > 19:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print('Classificação: {}'.format(categoria))
