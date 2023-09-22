galera = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(float(input('Insira o seu peso: ')))
    pessoa.append(str(input('Insira seu nome: ')))
    galera.append(pessoa[:])

    if len(galera) == 1:
        maior = menor = pessoa[0]

    else:
        #peso da pessoa > maior peso registrado
        if pessoa[0] > maior:
            maior = pessoa[0]
        
        if pessoa[0] < menor:
            menor = pessoa[0]

    pessoa.clear()
    continuar = str(input('Continuar? [S|N] '))
    if continuar in 'Nn':
        break

print(f'Foram registradas {len(galera)} pessoas.')
print(f'Maior peso: {maior}kg', end=' ')
for c in galera:
    if c[0] == maior:
        print(c[1], end=' ')
print(f'\nMenor peso: {menor}kg', end=' ')
for c in galera:
    if c[0] == menor:
        print(c[1], end=' ')

'''info = []
info.append('João')
info.append(21)

p = list()
p.append(info[:]) #lista composta: lista na lista
print(p)

p.clear() #limpa os dados 

a = [['Eu', 19], ['Maria', 15]]
print(a[1][0])
print(a[0]) #mostra todo o [0] = Eu, 19

teste = ['Gustavo', 40]
galera = []
galera.append(teste[:]) #É utilizado teste[:] e não somente teste para evitar
#aquele vínculo que se cria ao tentar copiar duas listas, portanto copia-se só o conteúdo
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

teste.clear() #limpa a lista
print(teste) #lista vazia'''
