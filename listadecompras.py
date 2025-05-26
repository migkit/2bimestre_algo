compras = ["pao"]
sair = "nao" 
while  sair == "nao" or sair == "n":
    
    resposta = input("deseja adicionar algum item? ")

    if resposta == "sim" or resposta == "s":
        produto = input("qual é o produto? ")
        compras.append(produto)

    elif resposta == "nao" or resposta == "n":
        input("voce nao adicionou nenhum produto")

        remover = input("deseja remover algo? ")
        if remover == "sim" or remover == "s":
            produto = input("qual produto deseja remover? ")
            compras.remove(produto)

        elif remover == "nao" or remover == "n":
            input("voce nao removeu nenhum produto")

    sair = input("deseja terminar a compra? ")

    print("lista de compras", compras)
