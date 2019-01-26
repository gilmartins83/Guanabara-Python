largura = float(input("A Largura da parede é: "))
altura = float(input("A Altura da parede é: "))
area = largura * altura
tinta = area / 2
print("Sua parede tem {} metros quadrados e precisará de {:.2f} litros de tinta" .format (area, tinta))