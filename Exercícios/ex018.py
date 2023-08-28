import math

ang = float(input('Insira um ângulo a seguir: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O ângulo {} possui seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}'.format(ang, seno, cosseno, tangente))