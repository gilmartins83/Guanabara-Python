real = float(input("Quanto tinheito você tem? R$ "))
us = real / 3.78
ca = real / 2.85
eu = real / 4.31
lb = real / 4.98
au = real / 2.71
ps = real / 0.0983
print("R$ {:.2f} reais equivale a: \n\nUS$ {:.2f} dólares americanos \nCAD$ {:.2f} dólares canadenses \n€$ {:.2f} euros \n£$ {:.2f} libras \nAUD$ {:.2f} dólares australianos \nPA$ {:.2f} pesos argentinos " .format( real, us, ca, eu, lb, au, ps))


print('               Casa de Câmbio BR')
print('-' * 50)
print('DADOS do Cliente')
print()
nome = input('Nome: ')
idade = input('Idade: ')
cpf = input('CPF: ')
telefone = input('Telefone: ')
print('-' * 30)
print('Dados do câmbio')
print()
real = float(input('Quanto você deseja trocar: R$ '))
print()
dolar = real / 3.27
euro = real / 3.67
libra = real / 4.37
print('Listamos alguns valores que você pode adquirir de acordo com a quantia que você deseja trocar')
print()
print('Com R$ {:.2f} você pode trocar por US$ {:.2f}'.format(real, dolar))
print('Com R$ {:.2f} você pode trocar por  €  {:.2f}'.format(real, euro))
print('com R$ {:.2f} você pode trocar por  £  {:.2f}'.format(real, libra))
print()
print('{} a BR Casa de Câmbio Agradece pela Preferência, Volte Sempre!'.format(nome))
print('-' * 70)