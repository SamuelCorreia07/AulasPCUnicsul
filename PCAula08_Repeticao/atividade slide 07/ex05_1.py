# media qtd indeterminada while
contador = 0
soma = 0
resp = "s"

while resp == "s" or resp == "S":
    num = float(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja continuar (S/N)?")

media = soma / contador
print("A media dos números digitados é %.2f" %media)