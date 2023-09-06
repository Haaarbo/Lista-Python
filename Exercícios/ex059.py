opcao = -1

n1 = int(input('Insira um valor a seguir: '))
n2 = int(input('Insira outro valor a seguir: '))

while opcao != 5:
    print("""Escolha uma das opções a seguir:
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos números
          [5] Sair do programa""")
    
    opcao = int(input('Sua opção: '))

    if opcao == 1:
        print('+'*15)
        print('{} + {} = {}'.format(n1, n2, n1+n2))
        print('+'*15)

    elif opcao == 2:
        print('x'*15)
        print('{} x {} = {}'.format(n1, n2, n1*n2))
        print('x'*15)

    elif opcao == 3:
        print('>'*15)
        if n1 > n2:
            print('O número maior é {}'.format(n1))
        elif n2 > n1:
            print('O número maior é {}'.format(n2))
        else:
            print('Ambos os números são iguais!')
        print('<'*15)
    
    elif opcao == 4:
        print('*'*15)
        print('Ok, liberando espaço da memória...')
        n1 = int(input('Insira um valor a seguir: '))
        n2 = int(input('Insira outro valor a seguir: '))
        print('*'*15)

    elif opcao == 5:
        print('-'*15)
        print('Ok! Encerrando o programa...')
        print('-'*15)

    else:
        print('!'*15)
        print('Opção inválida!')
        print('!'*15)
