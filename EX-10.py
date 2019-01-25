real = float(input("Quanto tinheito você tem? R$ "))
us = real / 3.78
ca = real / 2.85
eu = real / 4.31
lb = real / 4.98
au = real / 2.71
ps = real / 0.0983
print("R$ {:.2f} reais equivale a: \n\nUS$ {:.2f} dólares americanos \nCAD$ {:.2f} dólares canadenses \n€$ {:.2f} euros \n£$ {:.2f} libras \nAUD$ {:.2f} dólares australianos \nPA$ {:.2f} pesos argentinos " .format( real, us, ca, eu, lb, au, ps))
