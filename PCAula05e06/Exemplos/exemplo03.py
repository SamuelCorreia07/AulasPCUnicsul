num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

if num1 > num2 and num1 > num3:
    print("O primeiro número (%d) é o maior" %(num1))
elif num2 > num1 and num2 > num3:
    print("O segundo número (%d) é o maior" %(num2))
elif num3 > num1 and num3 > num2:
    print("O terceiro número (%d) é o maior" %(num3))