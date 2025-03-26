conta1 = float(input("Digite o valor da conta de luz: "))
conta2 = float(input("Digite o valor da conta de água: "))
conta3 = float(input("Digite o valor da conta de internet: "))
salario = float(input("Digite o valor do seu salário: "))

if salario < (conta1+conta2+conta3):
    print("Salário insuficiente para pagar as contas! FAZUELI")
else:
    salario -= conta1+conta2+conta3
    print("Valor após pagar as contas: R$%.2f" %(salario))