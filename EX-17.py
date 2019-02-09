'''co = float(input("comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f} " .format(hi))'''

import math
co = float(input("comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("A intpotenusa vai medir {:.2f}" .format(hi))
