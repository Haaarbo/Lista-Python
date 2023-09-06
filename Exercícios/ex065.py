qtd = int(input('Quantos números você gostaria de digitar? '))
i = 0 #numero para realizar o ciclo
total = 0 #soma de todos os números

while i < qtd:
    n = ('Insira um valor: ')

    if i == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
    total += n
    i += 1
