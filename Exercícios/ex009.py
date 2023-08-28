n = int(input('Insira um número a seguir: '))
i = 1

print('\n'+'*'*10)

for i in range(10):
    i += 1
    print('{} x {} = {}'.format(n, i, n*i))

print('*'*10)
