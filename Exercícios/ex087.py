l = [[], [], []]
somaP = soma3 = 0

for i in range(3):
    for j in range(3):
        valor = int(input(f'Valor {i}x{j}: '))
        l[i].append(valor)

        if valor % 2 == 0:
            somaP += valor
        if j == 2:
            soma3 += valor
        if i == 1:
            if j == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor

print('*'*25)
print('Matriz:')
for i in range(3):
    for j in range(3):
        print(f'[{l[i][j]}]', end='')
    print()
print('*'*25)

print('Dados da matriz:')
print(f'Soma dos pares: {somaP}')
print(f'Soma dos valores da terceira coluna: {soma3}')
print(f'Maior valor da segunda linha: {maior}')
