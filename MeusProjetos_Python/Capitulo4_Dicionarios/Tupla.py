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