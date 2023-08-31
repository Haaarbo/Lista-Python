num = int(input('Insira um número inteiro: '))
escolha = int(input("""Escolha entre uma das opções abaixo: 
    1 - Binário
    2 - Octal
    3 - Hexadecimal\n"""))

if escolha == 1:
    print('{} convertido para binário é {:b}'.format(num, num))
elif escolha == 2:
    print('{} convertido para octal é {:o}'.format(num, num))
elif escolha == 3:
    print('{} convertido para hexadecimal é {:x}'.format(num, num))
else:
    print('Hm, não identificamos essa opção! Finalizando o programa...')
