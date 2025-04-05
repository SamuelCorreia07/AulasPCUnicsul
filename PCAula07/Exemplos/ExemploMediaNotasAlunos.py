contador = 1
while contador <= 10:
    nota1 = float(input("Digite a primeira nota do aluno %d: " %(contador)))
    nota2 = float(input("Digite a segunda nota do aluno %d: " %(contador)))
    media = (nota1 + nota2) / 2
    print("A média do aluno %d é %.2f" %(contador, media))
    contador += 1