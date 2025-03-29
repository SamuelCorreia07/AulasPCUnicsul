digFinalPlaca = int(input("Insira o dígito final da placa do seu automóvel: "))

if digFinalPlaca == 1 or digFinalPlaca == 2:
    print("O veículo não pode circular nas segundas-feiras")
elif digFinalPlaca == 3 or digFinalPlaca == 4:
    print("O veículo não pode circular nas terças-feiras")
elif digFinalPlaca == 5 or digFinalPlaca == 6:
    print("O veículo não pode circular nas quartas-feiras")
elif digFinalPlaca == 7 or digFinalPlaca == 8:
    print("O veículo não pode circular nas quintas-feiras")
elif digFinalPlaca == 9 or digFinalPlaca == 0:
    print("O veículo não pode circular nas sextas-feiras")
else:
    print("Número inválido, digite apenas o último dígito da placa")
