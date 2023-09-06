somaIdade = 0
mulherMenor20 = 0
nomeMaisVelho = ''


for p in range(1, 5):
    nome = str(input('Insira o nome da {}a pessoa: '.format(p)))
    idade = int(input('Insira a idade da {} pessoa: '.format(p)))
    sexo = str(input('Insira o sexo(M|F) da {} pessoa: '.format(p)))

    #soma a idade para calcular a media depois
    somaIdade += idade

    #verifica se é mulher e tem menos de 20 anos, para somar o contador
    if idade < 20 and sexo in 'Ff':
        mulherMenor20 += 1
    
    #primeiramente verifica se é homem
    if sexo in 'Mm':
        #depois verifica se já há um nome atribuído à variável 'nomeMaisVelho' ou não
        if nomeMaisVelho == '':
            '''
            Se não houver um registro de qualquer homem atribuído à variável 'nomeMaisVelho',
            será atribuído como primeiro registro o nome e a idade, isto é, o primeiro registro
            de um homem será considerado já como mais velho, portanto, é salva sua idade e nome
            '''
            
            nomeMaisVelho = nome
            idadeMaisVelho = idade
        else:
            '''
            Se já houver um registro salvo de um homem mais velho, haverá também sua idade salva,
            portanto será comparada sua idade com a informada no momento do ciclo para verificar se
            a idade do ciclo agora é maior que a idade salva antes, se sim, a idade é atualizada
            '''
            if idade > idadeMaisVelho:
                nomeMaisVelho = nome
                idadeMaisVelho = idade

media = somaIdade/4
print('De acordo com a análise de dados, temos que:')
print('A média de idade do grupo é {:.1f} anos.'.format(media))
print('A quantidade de mulheres abaixo de 20 anos é {}.'.format(mulherMenor20))
print('O nome do homem mais velho é {}, que possui {} anos.'.format(nomeMaisVelho, idadeMaisVelho))
