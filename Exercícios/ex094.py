#definindo a lista l e o dicionario pessoas
lista = list()
pessoas = dict()

#estrutura de repetição geral, será parado quando nome = 0 
while True:
    nome = str(input('Nome (0 para sair): '))
    if nome in '0':
        break
    else:
        #ciclo para pedir o sexo, APENAS M ou F
        while True:
            sexo = str(input('Sexo [M|F]: '))
            if sexo not in 'MmFf':
                print('ERRO! Insira apenas M ou F!')
            else:
                break
        idade = int(input('Idade: '))

        #atribui cada um dos atributos capturados antes do fim do ciclo,
        #guardando-os no dicionário pessoas
        pessoas = {'Nome': nome,
                'Sexo': sexo,
                'Idade': idade}
        #a seguir, o primeiro endereço de memória haverá 1 "pessoa"
        lista.append(pessoas)

        #assim como o de sexo, para perguntar se continuará
        while True:
            continuar = str(input('Desejas continuar? [S|N] '))
            if continuar not in 'SsNn':
                print('ERRO! Insira apenas S ou N!')
            else:
                break
        if continuar in 'Nn':
            break


#pega o total de pessoas cadastradas
total = len(lista)

#contagem da média, soma-se todas as idades e divide-se pelo total
idadeTotal = 0
for p in lista:
    idadeTotal += p['Idade']
media = idadeTotal/total

#observa quem é mulher e guarda numa lista à parte, para printar depois
mulheres = list()
for p in lista:
    if p['Sexo'] in 'Ff':
        mulheres.append(p['Nome'])

#
idadeMaiorMedia = list()
for p in lista:
    if p['Idade'] > media:
        idadeMaiorMedia.append(p['Nome'])

#printa tudo
print('='*35)
print(f'A) Total de pessoas cadastradas: {total}')
print(f'B) Média de idade: {media:.2f}')
print('C) Mulheres:')
for m in mulheres:
    print(f'\t->{m}')
print('D) Pessoas acima da média:')
for acm in idadeMaiorMedia:
    print(f'\t->{acm}')
