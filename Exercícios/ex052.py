n = int(input('Informe um número: '))
cont = 0

for i in range(n):
    if n % (i+1) == 0:
        cont += 1

if cont == 2:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))
#print(cont)