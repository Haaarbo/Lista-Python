l = [] 
p = []
i = []
while True:
    n = int(input('Valor -> '))
    l.append(n)
    p.append(n) if n % 2 == 0 else i.append(n)
    continuar = str(input('Continuar? [S|N] '))
    if continuar in 'Nn':
        break

print(f'\nLista completa: {l}')
print(f'Lista de pares: {p}')
print(f'Lista de ímpares: {i}')
