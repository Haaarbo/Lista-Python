casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Anos de financiamento: '))

prestacao = casa/(anos*12)
print('A prestação da casa será de R${:.2f}'.format(prestacao))
if prestacao > (salario*0.3):
    print('Empréstimo negado! Prestação acima de 30% do salário')
else:
    print('Empréstimo aprovado!')