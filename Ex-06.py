n = int(input("digite um numero: "))
d = n * 2
t =  n * 3
r =  n ** (1/2)

print("o dobro de {} vale {} " .format (n, d))
print("o triplo de {} vale {} " .format (n, t))
print("a raiz quadrada de {} vale {} " .format (n, r))
print("\n")

print("O dobro de {} vale {} \no triplo vale {} \ne a raiz vale {}" .format (n, d, t, r))
print("\n")

print("O dobro de {} vale {} \no triplo vale {} \ne a raiz vale {}" .format (n, (n*2), (n*3), (n**(1/2))))
print("\n")

print("O dobro de {} vale {} \no triplo vale {} \ne a raiz vale {}" .format (n, (n*2), (n*3), (pow(n, (1/2)))))