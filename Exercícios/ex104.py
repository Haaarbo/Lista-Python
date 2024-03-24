def leiaInt():
    n = input('Digite um número: ')
    if n.isnumeric():
        print(f'Você digitou o número {n}')
    else:
        print(f'ERRO! Digite um número inteiro válido.')
        leiaInt()


#Programa principal
leiaInt()
