time = list()
jogador = dict()
partida = list()
while True:
    #definindo a estrutura dicionario JOGADOR com Nome, Partidas, Gols(lista) e Total(0)
    #importante ressaltar que o jogador que foi registrado anteriormente é apagado no clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totalPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0, totalPartidas):
        partida.append(int(input(f'\tQuantos gols na partidas {c+1}?  ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)


    #após a leitura dos dados do jogador, o mesmo é registrado ao time
    time.append(jogador.copy())
    #para o caso do user não escrever S ou N, repetirá o processo
    while True:
        cont = str(input('Gostaria de continuar? [S|N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda apenas com S (SIM) ou N (NÃO). Tenten novamente... \n\n')
        #para caso o user responda não, quebra o ciclo
    if cont == 'N':
        break

#cabeçalho
print('-='*20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

#mostrando o resultado
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='-')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca>= len(time):
        print('Erro! Não existe um jogador com esse ID no time! Tenten novamente...')
    else:
        print(f' ====> DADOS DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)

print('Volte sempre!')