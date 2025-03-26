compra = float(input("Digite o valor da compra: "))

if compra > 200:
    compra = compra * 0.8

print("Valor total da compra: R$%0.2f" %(compra))