l = []
cont = 0
while True:
    n = int(input('Valor -> '))
    cont += 1
    l.append(n)

    continuar = str(input('Continuar? [S|N] '))
    if continuar in 'Nn':
        break

l.sort(reverse=True) #inverte a ordem da lista
print(f'\nO usuário digitou {cont} números.')
print(f'Lista em ordem decrescente: {l}')
if 5 in l:
    print(f'O valor 5 foi digitado! e está na posição {l.index(5)+1}')
else:
    print('O valor 5 não se encontra na lista!')
