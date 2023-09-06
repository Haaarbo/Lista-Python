sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Insira o sexo: ')).strip().upper()[0]
print('Seu sexo é [{}].'.format(sexo))