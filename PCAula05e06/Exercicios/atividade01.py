salario = float(input("Digite o salário do colaborador: R$"))
if salario <= 280:
    percentual = 20
elif salario > 280 and salario <= 700:
    percentual = 15
elif salario > 700 and salario <= 1500:
    percentual = 10
elif salario > 1500:
    percentual = 5
else:
    print("Valor inserido inválido.")

print("Salário anterior: R$%.2f" %(salario))
print("Percentual de aumento aplicado: %d%%" %(percentual))
percentual = percentual/100
print("Valor do aumento: R$%.2f" %(salario * percentual))
print("Salário com reajuste: R$%.2f" %(salario * (1+percentual)))
