idade = int(input("Digite sua idade em dias:"))
ano = idade // 365
dias_meses = idade-(ano*360)
mes=dias_meses//30
dias=dias_meses-(mes*30)
print("Você tem {0} ano/s")
