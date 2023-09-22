turma = []
aluno = []

while True:
    aluno.append(str(input('Insira o nome do aluno: ')))
    
    n1 = int(input('Insira a 1a nota: '))
    n2 = int(input('Insira a 2a nota: '))
    media = (n1 + n2) / 2

    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)

    turma.append(aluno[:])
    aluno.clear()

    continuar = str(input('Continuar? [S|N] '))
    print('-'*30)
    
    if continuar in 'Nn':
        break

print(f'{"Nº":<4}', end='')
print(f'{"Nome":<13}', end='')
print(f'{"Média":>}')
print('-'*30)
for i in range(len(turma)):
    print(f'{i:<4}', end='')
    print(f'{turma[i][0]:<13}', end='')
    print(f'{turma[i][3]:>}')
    