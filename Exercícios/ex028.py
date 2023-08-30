from random import randint
from time import sleep

computador = randint(0, 5)
n = int(input('Adivinhe no número que pensei... '))
sleep(3)

if n == computador:
    print('\CERTO')
else:
    print('\nERRADO')

print('O número que pensei foi {}!'.format(computador))