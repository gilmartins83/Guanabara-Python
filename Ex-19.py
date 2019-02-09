'''import random
n1 = input("digite o nome do primeiro aluno: ")
n2 = input("digite o nome do segundo aluno: ")
n3 = input("digite o nome do terceiro aluno: ")
n4 = input("digite o nome do quarto aluno: ")
lista = (n1, n2, n3, n4)
escolhido = random.choice(lista)
print("O Aluno escolhido foi {}" .format(escolhido))'''

from random import choice
n1 = input("digite o nome do primeiro aluno: ")
n2 = input("digite o nome do segundo aluno: ")
n3 = input("digite o nome do terceiro aluno: ")
n4 = input("digite o nome do quarto aluno: ")
lista = (n1, n2, n3, n4)
escolhido = choice(lista)
print("O Aluno escolhido foi {}" .format(escolhido))
