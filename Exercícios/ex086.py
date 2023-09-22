l = [[], [], []]

for i in range(3):
    for j in range(3):
        valor = int(input(f'Valor para posição {i+1}x{j+1}: '))
        l[i].append(valor)

print('-'*25)
for i in range(3):
    for j in range(3):
        print(f'[{l[i][j]}]', end='')
    print()
