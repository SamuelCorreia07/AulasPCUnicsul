idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 11:
    print("Você é uma criança!")
elif idade >= 12 and idade <= 18:
    print("Você é um adolescente!")
elif idade >= 19 and idade <= 24:
    print("Você é um jovem!")
elif idade >= 25 and idade <= 40:
    print("Você é um adulto!")
elif idade >= 41 and idade <= 60:
    print("Você está na meia idade!")
elif idade >= 60 and idade <= 120:
    print("Você é um idoso!")
elif idade > 120:
    print("Parabéns, você é o ser humano vivo mais velho da Terra 'clap' 'clap'")
else:
    print("Não existe idade negativa!!!")