primeiro = 0
segundo = 1
n = 0

limite = int(input('Insira até que termo irá a sequência Fibonacci: '))

while n < limite:
    if n == 0:
        print('{}º termo: {}'.format(n+1, primeiro))
        n += 1
    elif n == 1:
        print('{}º termo: {}'.format(n+1, segundo))
        n += 1
    else:
        print('{}º termo: {}'.format(n+1, primeiro+segundo))
        n += 1
        aux = segundo
        segundo = aux + primeiro
        primeiro = aux
