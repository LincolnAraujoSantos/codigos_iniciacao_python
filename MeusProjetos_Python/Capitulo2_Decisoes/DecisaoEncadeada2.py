nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
covid19=input("Suspeita de Covid-19? ").upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO
if covid19=="SIM":
    print("Encaminhe o paciente para a sala AMARELA")
elif covid19=="NÃO":
    print("Encaminhe o paciente para a sala BRANCA")
else:
    print("Responda a suspeita de Covid-19 com SIM ou NÃO")

#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade>=65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")