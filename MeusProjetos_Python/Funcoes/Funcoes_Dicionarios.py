def perguntar():
    resposta = input("O que deseja realizar?\n" +
                     "<I> - Para Inserir um usuário\n"+
                     "<P> - Para Pesquisar um usuário\n"+
                     "<E> - Para Excluir um usuário\n"+
                     "<L> - Para Listar um usuário:\n").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o Login:\n").upper()] = [input("Digite o nome:\n").upper(),
                                                      input("Digite a útima data de acesso:\n"),
                                                      input("Qual a última estação acessada:\n").upper()]
def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome............:\n"+lista[0])
        print("Último acesso...:\n"+lista[1])
        print("Útilma estação..:\n"+lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......")
        print("Login:", chave)
        print("Dados:", valor)