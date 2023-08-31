from datetime import date

anoAtual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento
saldo = 18 - idade
alistamento = anoAtual + saldo

if idade < 18:
    print('Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(alistamento))
elif idade > 18:
    print('Já fazem {} ano(s) que passou do seu tempo de alistamento!'.format(abs(saldo)))
    print('Seu alistamento foi em {}.'.format(alistamento))
else:
    print('Seu alistamento será neste ano, de {}.'.format(alistamento))
