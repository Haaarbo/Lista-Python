def ficha(nome='<desconhecido>', qtdGols=0):
    print(f'O jogador {nome} fez {qtdGols} gol(s) no campeonato.')
    

#Programa principal
jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gol(s): '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(qtdGols=gols)
else:
    ficha(jogador, gols)