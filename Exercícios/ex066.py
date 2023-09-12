cont = soma = 0
while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f'O usuário inserio {cont} números, e a soma de todos eles é {soma}.')
