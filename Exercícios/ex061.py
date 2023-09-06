primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 0
termo = primeiro
while n < 10:
    print('{}º termo: {}'.format(n+1, termo))
    termo += razao
    n += 1
