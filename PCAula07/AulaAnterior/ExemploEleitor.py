idade = int(input("Digite sua idade: "))
if idade < 16: 
    categoria = "não-eleitor"
elif idade >= 18 and idade <= 65:
    categoria = "eleitor obrigatório"
else:
    categoria = "eleitor facultativo"
print("Sua classe eleitoral é:", categoria)