n = 0
soma = 0

while n != 999:
    n = int(input('Insira um valor: [999 para parar] ' ))
    if n != 999:
        soma += n

print('A soma de todos os números digitados é {}.'.format(soma))
