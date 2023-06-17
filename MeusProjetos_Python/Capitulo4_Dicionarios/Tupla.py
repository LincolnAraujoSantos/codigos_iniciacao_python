ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos:\n"),
         input("Digite os dois últimos octetos:\n"))]=input("Nome da máquina:\n")
    resp=input("Digite <S> para continuar:\n").upper()

#APROVEITANDO OS DADOS DA TUPLA
print("Exibindo ip's: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo máquinas com o mesmo endereço: \n")
pesquisa=input("Digite os dois últimos octetos: \n")
for ip, nome in ips.items():
    print("Máquina no mesmo endereço (redes diferentes)\n")
    if(ip[1]==pesquisa):
        print(nome)

print("Máquinas que compõem uma mesma rede:\n")
rede=input("Digite os dois primeiros octetos:\n")
for ip, nome in ips.items():
    if(ip[0]==rede):
        print(nome)


