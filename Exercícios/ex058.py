from random import randint
from time import sleep

computador = randint(0, 10)
n = -1
palpites = 0

while n != computador:
    n = int(input('Adivinhe no número que pensei... '))
    sleep(3)

    if n == computador:
        print('\nCERTO')
    else:
        print('\nERRADO')
    palpites += 1

print('O número que pensei foi {}!'.format(computador))
print('Você precisou de {} palpites para acertar!'.format(palpites))
