dias = int(input("quantos dias voce deseja alugar o carro? "))
km = float(input("Quantos kilometros você andou? "))
pago = dias * 60 + (km * 0.15)
print("o valor do aluguel do carro foi de R$ {:.2f}" .format(pago))

