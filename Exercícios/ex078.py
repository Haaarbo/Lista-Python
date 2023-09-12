l = []

for c in range(5):
    n = int(input('Insira um valor: '))
    l.append(n)

    if c == 0:
        maior = n
        menor = n
        posMaior = c
        posMenor = c

    else:
        if n > maior:
            maior = n
            posMaior = c
        if n < menor:
            menor = n
            posMenor = c

print('\nEntre os valores informados, temos que:')
print(f'O menor valor é {menor}, que está na posição {posMenor+1}.')
print(f'O maior valor é {maior}, que está na posição {posMaior+1}.')

'''

l = ['café da manhã', 'almoço', 'janta']
l.append('brunch') #adiciona um elemento na lista na última posição
print(l)

l.insert(0, 'lanche') #adiciona um elemento na lista na posição definida
print(l)

del l[0] #apaga o elemento da lista indicando a posição, diminuindo o tamanho da lista
l.pop(3) #mesma coisa de cima, geralmente o .pop() é usado para apagar o último elemento
l.remove('janta') #elimina a primeira ocorrência do elemento usando o próprio elemento como parâmetro
print(l)

v = list(range(2, 10))
print(v)

desordenado = [1, 4, 2, 89, 3, 0, -34]
print(desordenado)
desordenado.sort() #deixa em ordem crescente
print(desordenado)
desordenado.sort(reverse = True) #deixa em ordem decrescente
print(desordenado)

iniciar1 = [] #um jeito de inicializar uma lista
iniciar2 = list() #outro jeito

a = [1, 2, 3, 4]
b = a #ISSO É MUITO IMPORTANTE!

Ao atribuir que uma lista recebe outra, é criada uma CONEXÃO
ENTRE ELAS, onde ao sse alterar um elemento de um, é alterado necessariamente
do outro também!

Explicando melhor, pelo que compreendi, cria-se um vínculo no endereçamento
das variáveis, isto é, elas compartilham do mesmo espaço de memória!

Uma maneira para que não haja esse vínculo entre as listas, isto é, que a lista
receba somente os valores, é exemplificada na inicialização da variável c, utilizando
FATIAMENTO:

c = a[:] #c recebe TUDO de a

b[2] = 9 #alteração que afetará AMBAS AS LISTAS
print(f'Lista a: {a}') #[1, 2, 9, 4]
print(f'Lista b: {b}') #[1, 2, 9, 4]
print(f'Lista c: {c}') #[1, 2, 3, 4]

'''
