from random import randint

tupla = (randint(0, 10), 
         randint(0, 10), 
         randint(0, 10), 
         randint(0, 10), 
         randint(0, 10))

print('Os valores sorteados foram: ')
for pos, elemento in enumerate(tupla):
    print(elemento, end=' ')
    
    if pos == 0:
        maior = elemento
        menor = elemento
    else:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento

#print(f'\nO maior número foi {max(tupla)} e o menor foi {min(tupla)}.')
print(f'\nO maior número foi {maior} e o menor foi {menor}.')
