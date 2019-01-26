preco = float(input("Qual é o valor do produto? R$ "))
desconto = preco * 0.05
print("O desconto de 5% do produto foi de R$ {:.2f} e o produto custará R$ {:.2f}" .format (desconto, (preco-desconto)))