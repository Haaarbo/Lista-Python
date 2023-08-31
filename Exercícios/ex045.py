from random import randint

print("""Suas opções:
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA""")
jogador = int(input('Sua opção: '))
computador = randint(1, 3)

if jogador == computador:
    resultado = 'EMPATE'
elif jogador > computador or jogador == 1 and computador == 3:
    resultado = 'JOGADOR VENCEU'
else:
    resultado = 'JOGADOR PERDEU'

print('JO\nKEN\nPO\n!!!')
print('-='*18)
print('JOGADOR: {}'.format(jogador))
print('COMPUTADOR: {}'.format(computador))
print('-='*18)

print('Resultado:')
print(resultado)