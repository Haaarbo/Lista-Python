from random import randint
from time import sleep
from operator import itemgetter

ordem = list()
resultados = {'J1': randint(1, 6),
              'J2': randint(1, 6),
              'J3': randint(1, 6),
              'J4': randint(1, 6)
              }

for k, v in resultados.items(): #acessa o dicionario resultado
    print(f'{k} jogou o dado e tirou {v}!')
    sleep(1)

print(f'{"RANKING":-^29}')
ordem = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for pos, valores in enumerate(ordem):
    print(f'{pos+1}º lugar: {valores[0]} com {valores[1]} no dado!')
    sleep(1)
