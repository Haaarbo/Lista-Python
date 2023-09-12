from random import randint
from time import sleep

vitorias = 0
while True:
    computador = randint(0, 10)
    opcao  = str(input('Escolha se será PAR [P] ou ÍMPAR[I]: ')).strip().upper()[0]
    
    print('OK! Prepare-se!')
    sleep(1)
    print('1...')
    sleep(1)
    print('2...')
    sleep(1)
    print('3...')
    sleep(1)
    print('E...')

    jogador = int(input('JÁ: '))
    print(f'O computador jogou {computador}')

    soma = jogador + computador
    print(f'A soma entre a jogada do computador (\033[31m{computador}\033[m) e do jogador (\033[34m{jogador}\033[m) é \033[1;33m{soma}\033[m.')

    if opcao in 'Pp' and soma % 2 == 0 or opcao in 'Ii' and soma % 2 != 0:
        resultado = 'O JOGADOR VENCEU'
        vitorias += 1
    else:
        resultado = 'O JOGADOR PERDEU'
        break

    print(resultado)
    print('-'*20)


print(f'O jogador obteve {vitorias} consecutivas!')
