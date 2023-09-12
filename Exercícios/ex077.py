t = ('Estudar', 'Praticar', 
           'Leite', 'dinheiro',
           'Picadinho', 'livro',
           'Leite condensado', 'página',
           'Achocolatado', 'Python')

for palavras in t:
    print(f'\nNa palavra {palavras} se encontram as vogais: ', end='')
    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    