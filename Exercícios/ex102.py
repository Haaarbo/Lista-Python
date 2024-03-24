def fatorial(n, show=True):
    f = 1
    for i in range(1, n+1):
        f *= i
    if show:
        print(f'O fatorial de {n} é {f}.')



#Programa principal
numero = int(input('Informe um número: '))
fatorial(numero)
print('Fatorial calculado!')