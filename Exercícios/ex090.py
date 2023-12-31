aluno = {'nome': str(input('Qual o nome do aluno?\n')),
         'media': float(input('Qual a média do aluno?\n'))
}

if aluno['media'] < 5:
    print(f'O aluno {aluno["nome"]} está REPROVADO por conta da sua média {aluno["media"]}')
elif aluno['media'] > 7:
    print(f'O aluno {aluno["nome"]} está APROVADO por conta da sua média {aluno["media"]}')
else:
    print(f'O aluno {aluno["nome"]} está DE RECUPERAÇÃO por conta da sua média {aluno["media"]}')


for k, v in aluno.items():
    print(f'{k} é {v}')

'''dicionario = dict()
dicionario = {'nome': 'Abrahão',
              'idade': 21,
              'sexo': 'M'
              }
//no código acima, é criado um dicionário, em seguida de sua estrutura, contendo um atributo 'nome', 'idade' e 'sexo',
//e atribuindo a estes os valores 'Abrahão', 21, e 'M', respectivamente.

dicionario['isWake'] = True
//adiciona uma parte chamada 'isWake' e atribui um valor 'True' a este

print(dicionario['nome']) //printa 
print(dicionario['isWake'])
del dicionario['isWake'] //elimina o elemento 'isWake' e seu valor
print(f'O {dicionario["nome"]} tem {dicionario["idade"]}.')

print(dicionario.values()) #pega os VALORES
print(dicionario.keys()) #pega os nomes dos CAMPOS
print(dicionario.items()) #pega AMBOS

/*É possível usar os dicionários em ciclos for, como no exemplo abaixo:
n -> indica a chave, isto é, o nome do campo, por exemplo, 'nome'
i -> indica o valor atribuído à chave, isto é, 'Abrahão', por exemplo
dicionario.items() -> função que puxa os elementos/chaves e seus respectivos valores
*/
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