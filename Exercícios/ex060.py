n = int(input('Insira um número: '))
cont = n
fatorial = 1

while cont > 1:
    fatorial *= cont
    cont -= 1

print('O fatorial de {} é igual a {}.'.format(n, fatorial))

'''Outra forma de fazer:

from math import factorial

n = int(input('Insira um número: '))
f = factorial(n)
print('O fatorial de {} é igual a {}.'.format(n, f))

'''
