from random import randint

lista = []
jogos = []
qtd = int(input('Informe a quantidade de jogos a ser gerado: '))

for i in range(qtd):
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
    lista.append(jogos[:])
    jogos.clear()

print('-'*30)
for i in range(qtd):
    print(f'Jogo {i+1}: ')
    print(f'{lista[i]}')
print('-'*30)
