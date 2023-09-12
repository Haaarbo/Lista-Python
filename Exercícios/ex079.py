l = list()
while True:
    n = int(input('Valor: '))
    if n in l:
        print('Você já inseriu esse valor!')
    else:
        l.append(n)
    continuar = str(input('Continuar? [S|N] ')).strip()
    if continuar in 'Nn':
        break

l.sort()
print(f'Números digitados: {l}')
