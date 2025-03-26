numeros = [2,5,9,14,24,31,50]

print("Jogo: Adivinhe um número de 1 a 50")
numUsuario = int(input("Digite um número inteiro: "))

if numUsuario in numeros:
    print(f"Parabéns! O número {numUsuario} está na lista!")
else:
    print(f"Game Over! O número {numUsuario} não está na lista!")