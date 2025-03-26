import math

# exemplo 7 do slide: raiz quadrada

num = float(input("Digite um número: "))
if num > 0:
    r = math.sqrt(num)
    print("A raiz quadrada de ", num ," é: ", r)
else:
    print("Não é possível calcular raiz quadrada de número negativo")
