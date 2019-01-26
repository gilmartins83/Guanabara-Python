salario = float(input("Digite o salaro do funcionário? R$ "))
novo = salario + (salario * 0.15)
print("O aumento de 15% do salario foi de R$ {:.2f} e o funcionário passará a receber R$ {:.2f}" .format ((salario * 0.15), novo))
print("\n")
salario_chefe = float(input("Digite o antigo salário do chefe: R$ "))
novo_salario_chefe = float(input("Digite o novo salário do chefe: R$ "))
aumento = ((novo_salario_chefe - salario_chefe) / salario_chefe) * 100
print("O novo salário do chefe aumentou em {:.2f} %" .format(aumento))
print("\n")
imposto = float(input("Digite o valor do imposto pago anteriormente pela empresa: R$ "))
novo_imposto = float(input("Digite o novo valor do imposto reduzido: R$ "))
deducao = ((imposto - novo_imposto) / imposto) * 100
print("O novo valor do imposto caiu em {:.1f} % " .format(deducao))