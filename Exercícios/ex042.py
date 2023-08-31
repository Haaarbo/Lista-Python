l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('É possível formar um triângulo com os lados {}, {} e {}'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print('O triângulo formado é equilátero!')
    elif l1 != l2 != l3:
        print('O triângulo formado é escaleno!')
    else:
        print('O triângulo formado é isóceles!')
else:
    print('Os lados informados NÃO PODEM formar um triângulo!')