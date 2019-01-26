valorProduto = float(input('Qual é o valor do produto de compra? R$'))
modoPagamento = input('Deseja parcelar ou pagar à vista? ')

if modoPagamento == 'à vista' or modoPagamento == 'À vista':
    desconto = valorProduto - (valorProduto * 20 / 100)
    print('Certo! Nesse caso, você recebe-rá 20% de desconto.')
    print('O novo preço do produto é R${:.2f}'.format(desconto))

elif modoPagamento == 'parcelar' or modoPagamento == 'parcela':
    print('Certo! Pagamento parcelado. Segue abaixo tabela de parcelamentos:')
    print('=' * 10, 'Tabela', '=' * 10, '\n2 à 3 parcelas, acréscimo de 5%.\n4 à 6 parcelas, acréscimo de 10%.'
          '\n7 à 10 parcelas, acréscimo de 15%.\n11 parcelas ou mais, acréscimo de 25%.')
    parcela = int(input('Deseja fazer em quantas parcelas? '))

    if parcela <= 3:
        precoFinal = valorProduto + (valorProduto * 5) / 100
        valorParcela = precoFinal / parcela
        print('Certo! Você escolher fazer em {} vezes. Nesse caso, você receberá um acréscimo de 5% '
              'sobre o valor do produto.\nTotalizando {} parcelas de R${:.2f} com o preço final do '
              'produto de R${:.2f}'.format(parcela, parcela, valorParcela, precoFinal))

    elif parcela <= 6:
        precoFinal = valorProduto + (valorProduto * 10) / 100
        valorParcela = precoFinal / parcela
        print('Certo! Você escolheu fazer em {} vezes. Nesse caso, você receberá um acréscimo de 10%'
              ' sobre o valor do produto.\nTotalizando {} parcelas de R${:.2f} com o preço final do '
              'produto de R${:.2f}'.format(parcela, parcela, valorParcela, precoFinal))

    elif parcela <= 10:
        precoFinal = valorProduto + (valorProduto * 15) / 100
        valorParcela = precoFinal / parcela
        print('Certo! Você escolheu fazer em {} vezes. Nesse caso, você receberá um acréscimo de 15%'
              ' sobre o valor do produto.\nTotalizando {} parcelas de R${:.2f} com o preço final do '
              'produto de R${:.2f}'.format(parcela, parcela, valorParcela, precoFinal))
    else:
        precoFinal = valorProduto + (valorProduto * 25) / 100
        valorParcela = precoFinal / parcela
        print('Certo! Você escolheu fazer em {} vezes. Nesse caso, você receberá um acréscimo de 25%'
              ' sobre o valor do produto.\nTotalizando {} parcelas de R${:.2f} com o preço final do '
              'produto de R${:.2f}'.format(parcela, parcela, valorParcela, precoFinal))

else:
    print('Modo de pagamento inválido!')﻿