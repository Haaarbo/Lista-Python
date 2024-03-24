def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        resposta = 'NEGADO'
    elif 18 > idade >= 16 or idade > 70:
        resposta = 'OPCIONAL'
    else:
        resposta = 'OBRIGATÓRIO'

    return resposta


#Programa principal
nascimento = int(input('Informe seu ano de nascimento: '))
r = voto(nascimento)
print(f'Seu voto é: {r}.')

"""def contador(i, f, p):
    #docstring da função contador
    '''
    blablabla
    '''
    c = i
    while c<= f:
        print(f'{c }', end='')
        c += p
    print('FIM')


#Programa Principal
help(contador)

#Acessando docstrings e interactive help
'''help()
help(print)
print(print.__doc__)'''

#chamadas opcionais (considerando que na função foi constatado que a variavel tera algum valor "pardrão", p.e., p = 0):
def somar(a=0, b=0, c=0):
    s = a+b+c
    print(f'soma vale {s}')


somar(3,2,5)
somar(8,4)
somar()

#escopo global e local
def teste (b):
    
    A função teste serve como exemplo de como utilizar uma variável num ambiente local ser usada com seu valor globsal.

    "global a" muda o contexto de 'a' de local para global.

    Caso a função não tivesse esse comando, seria criado uma variável local 'a' com um valor 8, havendo assim um 'a' local e outro global.
    

    global a
    a = 8
    b+=4
    c=2
    print(f'a dentro={a}')
    print(f'b={b}')
    print(f'c={c}')

a=5
print(f'a fora antes da função = {a}')
teste(a)
print(f'a fora depois da função={a}')
help(teste)
"""