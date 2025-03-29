
nomeProduto = str(input("Digite o nome do produto: "))
valorCompra = float(input("Digite o valor de Compra: R$"))

if valorCompra > 0 and valorCompra < 10:
    percentual = 70
elif valorCompra >= 10 and valorCompra < 30:
    percentual = 50
elif valorCompra <= 30 and valorCompra < 50:
    percentual = 40
elif valorCompra >= 50:
    percentual = 30
else:
    print("Valor de compra inválido.")

lucroProduto = valorCompra * (percentual/100)
valorVendaProduto = valorCompra + lucroProduto

print("Nome do produto:", nomeProduto)
print("Lucro: R$%.2f" %(lucroProduto))
print("Valor de venda do produto: R$%.2f" %(valorVendaProduto))