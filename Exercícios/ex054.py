from datetime import date
atual = date.today().year
tMaior = 0
tMenor = 0

for p in range(1, 8):
    nasc = int(input('Em que ano {}a pessoa nasceu? '.format(p)))
    idade = atual - nasc

    if idade >= 21:
        tMaior += 1
    else:
        tMenor += 1

print('Há {} pessoas maiores de idade!'.format(tMaior))
print('Há {} pessoas menores de idade!'.format(tMenor))
