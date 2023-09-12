while True:
    n = int(input('Insira um número a seguir: '))
    if n < 0:
        break
    else:
        for i in range(11):
            print(f'{n} x {i} = {n*i}')
