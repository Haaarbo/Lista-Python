from datetime import datetime
pessoa = {'Nome': str(input('Qual seu nome? ')),
          'CTPS': str(input('Qual sua CTPS? (0 se não tiver) '))
          }

#idade da pessoa
nascimento = int(input('Qual seu ano de nascimento? '))
pessoa['Idade'] = datetime.now().year - nascimento

#pegando dados da CTPS
if pessoa['CTPS'] != '0':
    pessoa['Contrato'] = int(input('Qual ano da sua contratação? '))
    pessoa['Salário'] = float(input('Qual seu salário? R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (pessoa['Contrato'] + 35) - datetime.now().year


for k, v in pessoa.items():
    print(f'{k}: {v}')


#nome
#anoNascimento
#ctps (0 se n tiver
#      se n, + ano da contratação + salário)
#quantos anos vai se aposentar*/
