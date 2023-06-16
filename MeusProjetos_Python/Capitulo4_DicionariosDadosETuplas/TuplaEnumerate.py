usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail:\n").lower())
    resp=input("Digite <S> para continuar:\n").upper()

#ACRESCENTAR E ENUMERAR OS EMAILS CADASTRADOS EM UMA LISTA
tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome:\n"), input("Digite o nível:\n")]

for chave,dado in usuarios.items():
    print("Usuário..:", chave[0])
    print("Email....:", chave[1])
    print("Nome.....:", dado[0])
    print("Nível....:", dado[1])
    print() #ADICIONA UMA LINHA EM BRANCO APOS CADA ITEM DA CHAVE