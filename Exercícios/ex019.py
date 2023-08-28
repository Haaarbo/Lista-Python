from random import choice

a1 = input('Insira o nome de um aluno: ')
a2 = input('Insira outro nome: ')
a3 = input('Insira mais um nome: ')
a4 = input('Insira um último nome: ')

lista = [a1, a2, a3, a4]
sorteado = choice(lista)

print('O aluno sorteado foi {}!'.format(sorteado))