cont18 = contMulheres20 = contHomens = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M|F]: ')).strip()[0]
    
    if idade > 18:
        cont18 += 1
    if sexo in 'Mm':
        contHomens += 1
    if sexo in 'Ff' and idade < 20:
        contMulheres20 += 1

    continuar = str(input('Continuar? [S|N]')).strip()[0]
    if continuar in 'Nn':
        break

print('Dados coletados:\n')
print(f'Pessoas com mais de 18 anos: {cont18}')
print(f'Homens cadastrados: {contHomens}')
print(f'Mulheres com menos de 20 anos: {contMulheres20}')
