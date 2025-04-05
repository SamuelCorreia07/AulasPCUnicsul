n = int (input("Digite um número inteiro: "))
x = 1

print("A tabuada de %d é:" %(n))
while x <= 10:
    print("%d * %d = %d" %(n, x, (n*x)))
    x = x + 1