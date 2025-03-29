print("Tipos da diária:"
"\nS - Quarto Simples - R$ 255,50"
"\nD - Quarto Duplo - R$ 305,50"
"\nT - Quarto Triplo - R$ 360,50")

qtdDiaria = int(input("Digite a quantidade de diárias que deseja: "))
tipoDiaria = str(input("Digite o tipo da diária: "))

if tipoDiaria == "S" or tipoDiaria == "s":
    print("O valor total da hospedagem é R$%.2f" %(255.5 * qtdDiaria))
elif tipoDiaria == "D" or tipoDiaria == "d":
    print("O valor total da hospedagem é R$%.2f" %(305.5 * qtdDiaria))
elif tipoDiaria == "T" or tipoDiaria == "t":
    print("O valor total da hospedagem é R$%.2f" %(360.5 * qtdDiaria))
else:
    print("Tipo de diária inválido")
    