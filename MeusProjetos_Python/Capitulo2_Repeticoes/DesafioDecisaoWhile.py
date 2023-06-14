nome=input("Digite seu nome: ")
resposta="SIM"
while resposta=="SIM":
    nivel=input("Digite o nivel de acesso: ").upper()
    if nivel=="ADM" or nivel=="USR":
        genero=input("Digite o seu gênero: ").upper()
        if nivel=="ADM":
            if genero=="FEMININO":
                print("Olá administradora " + nome)
            else:
                print("Olá administrador " + nome)
        else:
            if genero=="FEMININO":
                print("Olá usuária " + nome)
            else:
                print("Olá usuário " + nome)
    elif nivel=="GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    resposta=input("Digite SIM para continuar: ").upper()