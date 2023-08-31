primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for n in range(10):
    termo = primeiro + n*razao
    print('{}º termo: {}'.format(n+1, termo))