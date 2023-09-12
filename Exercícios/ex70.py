total = maior1000 = precoBarato = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))

    total += preco
    if preco > 1000:
        maior1000 += 1
    
    if precoBarato == 0:
        precoBarato = preco
        nomeBarato = nome
    else:
        if preco < precoBarato:
            precoBarato = preco
            nomeBarato = nome
    
    continuar = str(input('Continuar? [S|N] ')).strip()[0]
    if continuar in 'Nn':
        break

print('-'*15)
print('Dados obtidos:\n')
print(f'Total: R${total}')
print(f'Quantidade de produtos acima de R$1000: {maior1000}')
print(f'Nome do produto mais barato: {nomeBarato} (R${precoBarato})')
