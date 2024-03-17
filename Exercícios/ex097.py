def escreva(m):
    print('~'*(len(m)+4))
    print(f'  {m}')
    print('~'*(len(m)+4))


#Programa Principal
msg = str(input('Insira uma mensagem de texto a seguir: '))
escreva(msg)