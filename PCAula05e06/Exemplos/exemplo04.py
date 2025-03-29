valorCompra = float(input("Digite o valor da compra: R$ "))
desconto = float(input("Desconto (em %) para essa compra: "))
desconto = desconto / 100

print("Valor inicial: R$%.2f" %(valorCompra))
print("Desconto ganho: R$%.2f" %(valorCompra*desconto))
print("Valor com desconto: R$%.2f" %(valorCompra * (1-desconto)))