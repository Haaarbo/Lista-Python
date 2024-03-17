def area(l, c):
    a = l * c
    print(f'A área do terreno {l} m x {c} m é de {a:.2f} m².')


#Programa Principal
print(f'{"Controle de Terrenos":^30}')
print('-'*30)
largura = float(input('Largura do terreno (m): '))
comprimento = float(input('Comprimento do terreno (m): '))
area(largura, comprimento)
'''def soma(a, b):
    s = a+b
    print(f'A soma de {a} + {b} é {s}')

#Programa Principal
soma(4,6)
soma(5,1)
soma(1,0)
soma(a=2, b=6)
soma(b=8, a=2)
print('-'*40)

#Empacotamento
Em Python, você tem a possibilidade de receber um parâmetro não necessário para ser recebido. Um exemplo: você tem uma função "contador()", na qual você precisa contar a quantidade de números recebidos. Nesse tipo de situação a quantidade de parâmetros pode variar bastante. Para isso, usa-se o termo * antes da variável para "desempacotar" todos os possíveis valores:

def contador(*n):
    tamanho = len(n)
    print(f'Recebi os valores {n} e são ao todo {tamanho} número(s).')

#Programa Principal
    
contador(2, 1, 7)
contador(0,0)
contador(1, 5, 6, 1, 3)


print('-'*40)
def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#Programa Principal
valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)


print('-'*40)
def soma2 (*valores):
    s=0
    for n in valores:
        s+= n
    print(f'Somando os valores {valores} temos {s}')


#Programa Principal
soma2(2,9,5)
soma2(5,6)'''