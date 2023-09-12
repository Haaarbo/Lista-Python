contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito',
            'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')

entrada = int(input('Insira um número: '))
print(f'\033[31m{entrada}\033[m --> \033[34m{contagem[entrada-1]}\033[m')




"""tupla = 'palavra 1', 'coisa 2', 'bagulho 3'
for c in tupla:
    print(c)
for pos, elemento in enumerate(tupla):
    print(f'A tupla {elemento} está na posição {pos}')
for cont in range(tupla):
    print(f'O cont está na posição {cont}, indicando, em tupla, o elemento {tupla[cont]}')
print('\n\n')
a = (1, 2)
b = (3, 4, 5)

c = b+a
e = sorted(c) #em ordem
print(e) 
print(f'O número 5 aparece {c.count(5)} vezes na tupla c') #quantas vezes aparece o 5
print(c.index(3)) #indica o índice onde está o elemento em parênteses
del(c) #deleta c"""
