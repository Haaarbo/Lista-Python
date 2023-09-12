produto = ('Pão', 1, 
           'Leite', 16.00,
           'Picadinho', 23.00,
           'Leite condensado', 7.50,
           'Achocolatado', 9.09)

print('-'*35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-'*35)

for pos in range(0, len(produto)):
    if pos % 2 == 0:
        print(f'{produto[pos]:.<21}', end='')
    else:    
        print(f'R${produto[pos]:>.2f}')
