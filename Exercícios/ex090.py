aluno = {'nome': str(input('Nome: ')),
         'media': float(input('Média: '))}

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'REPROVADO'
    
print(f'O aluno {aluno["nome"]} possui a média {aluno["media"]}, portanto, está {aluno["situacao"]}!')

'''dicionario = dict()
dicionario = {'nome': 'Abrahão',
              'idade': 21,
              'sexo': 'M'
              }
dicionario['isWake'] = True

print(dicionario['nome'])
print(dicionario['isWake'])
del dicionario['isWake']
print(f'O {dicionario["nome"]} tem {dicionario["idade"]}.')

print(dicionario.values()) #pega os VALORES
print(dicionario.keys()) #pega os nomes dos CAMPOS
print(dicionario.items()) #pega AMBOS

for n, i in dicionario.items():
    print(f'{n} -> {i}')


#ex de lista com dicionários dentro:
brasil = list()
e1 = {'uf': 'Amazonas', 'sigla': 'AM'}
e2 = {'uf': 'Pará', 'sigla': 'PA'}
brasil.append(e1)
brasil.append(e2)
print(f'A sigla de {brasil[0]["uf"]} é {brasil[0]["sigla"]}.')
print(f'A sigla de {brasil[1]["uf"]} é {brasil[1]["sigla"]}.')

brasil.clear() #limpando para aplicar outro exemplo

brasil = list()
estado = {} #outra forma de criar dicionario
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    estado.clear()
for e in brasil: #entrando na lista, pega-se um dicionário
    for k, v in e.items(): #entrando em cada dicionário, pega-se os itens
        print(f'O campo {k} tem valor {v}.')
'''