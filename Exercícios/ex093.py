#definindo a estrutura dicionario JOGADOR com Nome, Partidas, Gols(lista) e Total(0)
jogador = {'Nome': str(input('Nome do jogador: ')),
           'Partidas': int(input(f'Quantas partidas o jogador jogou? ')),
           'Gols': list(),
           'Total': 0}

#ciclo for para pegar os gols e somando os gols para pegar o total
for n in range(jogador['Partidas']):
    jogador['Gols'].append(int(input(f'\t->Gols da partida {n}: ')))
    jogador['Total'] += jogador['Gols'][n]

#printando resultado da forma tradicional
print()
print('='*35)

print(jogador)

print('='*35)

#printando resultado da segunda forma
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('='*35)

#printando resultado da terceira forma
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]}:')

for g in range(len(jogador['Gols'])):
    print(f'\t->Na partida {g}, fez {jogador["Gols"][g]} gol(s).')

print(f'\nFoi um total de {jogador["Total"]} gol(s).')

'''Poderia ser feito também o ciclo for da seguinte forma:

for i, v in enumerate(jogador['Gols']):
    print(f'\t->Na partida {i}, fez {v} gol(s).')'''
