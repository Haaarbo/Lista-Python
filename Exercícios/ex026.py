frase = str(input('Fale algo: ')).strip()

contador = frase.lower().count('a')
primeiro = frase.find('a')+1
ultimo = frase.rfind('a')+1

print(contador)
print(primeiro)
print(ultimo)