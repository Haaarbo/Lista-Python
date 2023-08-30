km = int(input('Insira a distância da viagem: '))

preco = km*0.5 if km <= 200 else km*0.45
print('O valor da viagem é R${}'.format(preco))
