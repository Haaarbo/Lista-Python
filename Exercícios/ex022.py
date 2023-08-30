nome = str(input('Informe seu nome completo: ')).strip()

nomeDividido = nome.split()

print('Seu nome em caixa alta é {}'.format(nome.upper()))
print('Seu nome em caixa baixa é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.strip()) - nome.count(' ')))
print('Seu primeiro nome é {} e possui {} letras'.format(nomeDividido[0], len(nomeDividido[0])))