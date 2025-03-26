import math

print("-----------Exemplo 01 -----------")
num = int(input("Digite um número com três digitos: "))
d1 = num // 100
d2 = num % 100 // 10
d3 = num % 10
inverso = d3*100+d2*10+d1
print("O inverso do número digitado é ", inverso)
print("---------------------------------")
print("-----------Exemplo 02 -----------")
num = float(input("Digite um número para saber sua raiz quadrada: "))
resultado = math.sqrt(num)
print("O valor da raiz quadrada é:", resultado)
print("---------------------------------")