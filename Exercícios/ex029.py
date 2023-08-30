velocidade = int(input('Qual a velocidade atual do carro? '))
multa = (velocidade-80)*7
if velocidade <= 80:
    print('Ok, boa tarde!')
else:
    multa = (velocidade-80)*7
    print('Você foi multado em R${}, 00!'.format(multa))