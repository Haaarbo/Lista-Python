l = []
for c in range(5):
    n = int(input('Valor: '))
    if c == 0:
        l.append(n)
    else:
        cont = 0

        for pos in range(len(l)):
            if n < l[pos]:
                l.insert(pos, n)
                break
            else:
                cont += 1 #conta quantas vezes n < l[pos] foi falso

        if cont == len(l): #se em nenhuma vez n foi menor que l[pos] durante toda a lista:
            l.append(n) #adiciona o elemento na última posição

print(f'Lista ordenada: {l}')
