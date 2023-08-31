from time import sleep

segundos = 10
for c in range(segundos, 0, -1):
    print('{} segundos!'.format(c))
    sleep(1)
print('KABOOOM!!!')