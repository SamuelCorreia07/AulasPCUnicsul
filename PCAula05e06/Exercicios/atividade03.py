valorOriginal = float(input("Digite o valor do produto: R$"))
percentualDesconto = int(input("Digite a % de desconto do produto: "))

valorDesconto = valorOriginal * (percentualDesconto/100)
valorFinal = valorOriginal - valorDesconto

print("Valor original do produto: R$%.2f" %(valorOriginal))
print("Desconto ganho: R$%.2f" %(valorDesconto))
print("Valor com desconto: R$%.2f" %(valorFinal))