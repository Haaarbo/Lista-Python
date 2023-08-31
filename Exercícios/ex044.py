compras = float(input('Valor das compras: R$'))
print("""Escolha sua forma de pagamento:
      [1] À vista em dinheiro vivo/cheque: 10% de desconto
      [2] À vista no cartão: 5% de desconto
      [3] Parcelado 2x: valor original
      [4] Parcelado em 3x ou mais: 20% de juros""")

opcao = int(input('Opção escolhida: '))

if opcao == 1:
    final = compras - (compras*0.1)
    print('Valor final: R${:.2f}'.format(final))
elif opcao == 2:
    final = compras - (compras*0.05)
    print('Valor final: R${:.2f}'.format(final))
elif opcao == 3:
    final = compras / 2
    print('Valor final: 2x de R${:.2f}'.format(final))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    final = compras / parcelas
    print('Valor final: {}x de R${:.2f}'.format(parcelas, final))
else:
    print('Opção inválida!')