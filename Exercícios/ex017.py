from math import hypot

oposto = float(input('Insira o comprimento do cateto oposto: '))
adjacente = float(input('Insira o comprimento do cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa do triângulo é {:.2f}'.format(hipotenusa))