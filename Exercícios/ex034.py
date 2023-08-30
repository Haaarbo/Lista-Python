antigoSalario = float(input('Insira seu salario: '))

novoSalario = antigoSalario + (antigoSalario*0.15) if antigoSalario <= 1250 else antigoSalario + (antigoSalario*0.10)

print('O novo salário é: R${:.2f}'.format(novoSalario))
