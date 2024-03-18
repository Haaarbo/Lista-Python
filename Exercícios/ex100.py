from random import randint
from time import sleep
numeros = list()


def sorteia():
    print('Iniciando sorteio:')
    for i in range(5):
        numeroSorteado = randint(1,10)
        print(f'{numeroSorteado} ', end='', flush='True')
        sleep(0.5)
        numeros.append(numeroSorteado)
    print('FIM')
    somaPar(numeros)


def somaPar(l):
    totalPares = 0
    for n in l:
        if n % 2 == 0:
            totalPares += n
    
    print(f'O total da soma de pares da lista {l} é {totalPares}.')



#Programa Principal
sorteia()
