largura = float(input('Insir a largura da parede: '))
altura = float(input('Agora a altura: '))

area = largura*altura
tinta = area/2

print('Para sua parede {:.2f}m x {:.2f}m, área {:.2f}, é necessário {:.2f} litros de tinta, aproximadamente.'.format(largura, altura, area, tinta))