l = [[], []]

for c in range(7):
    valor = int(input('Valor: '))
    if valor % 2 == 0:
        l[0].append(valor) #adicionando na lista de pares
    else:
        l[1].append(valor) #adicionando na lista de ímpares
    
l[0].sort()
l[1].sort()
print('='*25)
print(f'Pares: {l[0]}')
print(f'Ímpares: {l[1]}')
