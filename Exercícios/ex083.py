p = str(input('Insira uma expressão: '))
c1 = c2 = 0

print(p)

if '(' and ')' in p and p.count('(') == p.count(')'): #se sim, tem a mesma qnt?
        for pos in range(len(p)):
            if p[pos] == '(': 
                c1 += 1
                if c1 > c2:
                    resultado = True
                else:
                    resultado = False
                    break
            elif p[pos] == ')':
                c2 += 1
else:
    resultado = False

print(f'O uso dos parênteses é {resultado}')
