km = float(input('Quantos km rodados? '))
dias = int(input('Por quantos dias foi alugado? '))

preco = ((60*dias) + (0.15*km))

print('O valor a ser pago é R${:.2f}'.format(preco))