from time import sleep


def contador(start, end, step):
    if start > end:
        step *= -1
    for i in range(start, end, step):
        #IMPORTANTE: nas versões mais novas, o sleep está sendo aplicado sem aparecer propriamente o resultado de meio em meio segundo
        #Para ajustar que o sleep atue com o resultado a cada tantos segundos, ative o FLUSH para TRUE no PRINT
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')
    print('=-'*30)


print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)

print('Contagem de 10 até 0 de 2 em 2')
contador(10, -1, 2)

print('Agora é com você!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
print('OBS.: NÃO USE NÚMEROS NEGATIVOS')
while True:
    passo = int(input('Passo: '))
    if inicio and fim and passo > 0:
        break
    print('Atenção, não use números negativos! Tente novamente...')

contador(inicio, fim, passo)
