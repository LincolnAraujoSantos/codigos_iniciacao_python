# Começando nossa ferramenta
usuarios = {}
opcao = input("O que deseja realizar?\n" +
            "<I> - Para inserir um novo usuário\n" +
            "<P>  - Para Pesquisar um usuário\n" +
            "<E> - Para Excluir um usuário\n" +
            "<L> - Para Listar um usuário:\n ").upper()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        # substituicao das linhas 14a19.conferir arquivo ManagerUsers.py
        usuarios[input("Digite o login:").upper()] = [input("Digite o nome: ").upper(),
                                                      input("Digite a última data de acesso: "),
                                                      input("Qual a última estação acessada: ").upper()]
        # assim reduzimos nosso codigo

        opcao = input("O que deseja realizar?\n" +
            "<I> - Para inserir um novo usuário\n" +
            "<P>  - Para Pesquisar um usuário\n" +
            "<E> - Para Excluir um usuário\n" +
            "<L> - Para Listar um usuário: ").upper()
