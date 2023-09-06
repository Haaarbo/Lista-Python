primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 0
total = 10
opcao = -1


while n < total:
    termo = primeiro + n*razao
    print('{}º termo: {}'.format(n+1, termo))
    n += 1

while opcao != 0:
    opcao = int(input('Você gostaria de mostrar mais quantos termos? '))
    if opcao != 0:
        total += opcao
        while n < total:
            termo = primeiro + n*razao
            print('{}º termo: {}'.format(n+1, termo))
            n += 1
