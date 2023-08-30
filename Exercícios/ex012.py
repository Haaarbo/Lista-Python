preco = float(input('Insira o preco original a seguir: '))
desconto = 5

novoPreco = preco-(preco*desconto/100)

print('Com {}% de desconto, o novo preço é R${}'.format(desconto, novoPreco))