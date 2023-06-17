def chamarMenu():
    escolha = int(input("Digite:\n"
                        "<1> para registrar ativo\n"
                        "<2> para persistir em arquivo\n"
                        "<3> para exibir ativos armazenados:\n"))
    return escolha


def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização:\n"),
            input("Digite a descrição:\n"),
            input("Digite o departamento:\n")]
        resp = input("Digite <S> para continuar.\n").upper()


def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "")
        return "Persistido com sucesso!\n"


def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readline()
    return linhas
