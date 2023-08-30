nome = str(input('Nome completo: ')).strip()
nomeFrag = nome.split()
print('Muito prazer em conhecê-lo!')
print('Seu primeiro nome é {} e seu último é {}.'.format(nomeFrag[0], nomeFrag[len(nomeFrag)-1]))
