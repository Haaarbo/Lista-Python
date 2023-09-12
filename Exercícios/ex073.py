brasileirao = ('Botafogo', 'Palmeiras', 'Grêmio',
               'Flamengo', 'Fluminense', 'Bragantino',
               'Athletico-PR', 'Fortaleza', 'Atlético-MG',
               'Cuiabá', 'São Paulo', 'Cruzeiro',
               'Corinthians', 'Internacional', 'Goiás',
               'Bahia', 'Santos', 'Vasco da Gama', 
               'América-MG', 'Coritiba')

ordem = sorted(brasileirao)

#print(f'Lista: '{brasileirao})

#print(f'5 primeiros: {brasileirao[0:5]}')
print('Os primeiros 5 colocados são: ')
for time in range(5):
    print(brasileirao[time], end=' -- ')

#print(f'4 últimos: {brasileirao[-4:]}')
print('\n\nOs útlimos 4 colocados são: ')
for time in range(-4, 0):
    print(brasileirao[time], end=' -- ')

#print(f'Em ordem: {sorted(brasileirao)}')
print('\n\nOs times em ordem alfabética:')
for posicao, time in enumerate(ordem):
    print(f'{time}', end=' -- ')

print('\n\n')

#print(f'Posição da Chapecoense: {brasileirao.index("Chapecoense")+1}')
if 'CHAPECOENSEchapecoense' in brasileirao:
    posicao = brasileirao.index('Chapecoense')
    print(f'Chapecoense está na posição {posicao}')
else:
    print('Chapecoense não está no Brasileirão série A!')
