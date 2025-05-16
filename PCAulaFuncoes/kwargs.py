def saudacao(**kwargs):
    if 'nome' in kwargs:
        print(f"Olá, {kwargs['nome']}!")
    else:
        print("Olá, visitante!")
saudacao(nome="Maria")
saudacao()