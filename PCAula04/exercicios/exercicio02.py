turno = int(input("Digite seu turno de trabalho: "))
hrsTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))

if turno == hrsTrabalhadas:
    salario = float(hrsTrabalhadas*45)
else:
    salario = float(hrsTrabalhadas*37.5)

print("Salário = R$%0.2f" %(salario))