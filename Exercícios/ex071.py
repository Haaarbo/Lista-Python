print('*'*20)
print('BEM-VINDO(A) AO CAIXA ELETRÔNICO')
print('*'*20)
print('Cédulas disponíveis: R$1 | R$10 | R$20 | R$50\n')

n = valor = int(input('Valor a ser sacado: R$'))
nota = 50
cont = 0

while True:
    if n >= nota:
        n -= nota
        cont += 1
    else:
        print(f'{cont} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        
        cont = 0

        if n == 0:
            break
