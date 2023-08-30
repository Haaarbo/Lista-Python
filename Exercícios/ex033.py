n1 = int(input('Insira um valor: '))
n2 = int(input('Insira um outro valor: '))
n3 = int(input('Insira um terceiro valor: '))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3 

print('{} -> menor valor'.format(menor))

maior = n1

if n2 > n1 and n2 > n3:
    menor = n2
if n3 > n1 and n3 > n2:
    menor = n3 

print('{} -> maior valor'.format(maior))