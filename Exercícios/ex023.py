numero = str(input('Insira um número de 0 a 9999: '))
i = 0

for i in range(len(numero)):
    print('Dígito {}: {}'.format(i+1, numero[i]))
    i += 1