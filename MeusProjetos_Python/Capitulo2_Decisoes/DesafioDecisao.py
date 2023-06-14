#ADM - Ola administrador ou adminsitradora
#USR - ola usuario ou usuaria
#GUESt - Ola visitante
#se o nivel nao for nenhum desse devera exibir Ola desconhecido

nome=input("Digite seu nome: ")
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
