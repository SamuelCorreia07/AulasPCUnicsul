def apresentar_pessoa(**info):
    print("Informações da Pessoa:")
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
# Chamando a função com diferentes informações
apresentar_pessoa(nome="Mariana", idade=30, profissao="Desenvolvedora")
print("-" * 25)