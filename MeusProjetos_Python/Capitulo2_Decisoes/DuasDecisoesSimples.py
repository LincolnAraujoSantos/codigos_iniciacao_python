#Nunca faça essa utilização: tomada de duas decisoes simples
#opte sempre pela decisão composta

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=65:
    print("O paciente " + nome + " Possui atendimento prioritário!")
if idade <65:
    print("O paciente " + nome + " Não possui atendimento prioritário")