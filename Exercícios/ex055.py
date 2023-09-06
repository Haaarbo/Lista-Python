peso = float(input('Insira o primeiro peso a seguir: '))
maior = peso
menor = peso

for p in range (1, 5):
    peso = float(input('Insira outro peso a seguir: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O menor peso informado foi {}kg'.format(menor))
print('O maior peso informado foi {}kg'.format(maior))
