l1 = float(input('Insira um número: '))
l2 = float(input('Insira outro número: '))
l3 = float(input('Insira mais um número: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos NÃO podem formar um triângulo!')
