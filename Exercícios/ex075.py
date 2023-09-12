t = (int(input('Insira um valor: ')),
     int(input('Insira outro valor: ')),
     int(input('Insira mais um valor: ')),
     int(input('Insira o último valor: '))
)

print(f'\nO número \033[31m9\033[m apareceu \033[33m{t.count(9)}\033[m vezes.')

if 3 in t:
    print(f'O primeiro \033[31m3\033[m apareceu primeira vez na posição \033[33m{t.index(3)+1}\033[m.')
else:
    print(f'O número \033[31m3\033[m não aparece na lista!')
print('Os números pares são: ')

'''
for elemento in t:
    if n % 2 == 0:
        print(elemento, end=' ')
'''
for pos, elemento in enumerate(t):
    if elemento % 2 == 0:
        print(elemento, end=' ')
