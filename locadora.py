
def obterQuantidadeFilmes(filmes):
    print("Atualmente temos", len(filmes), "filme(s).")

def substituirFilme(filmes):
    posicao = int(input("Digite a posição do filme a ser substituído: "))

    if posicao > 0 and posicao <= len(filmes):
        novoNomeFilme = input("Digite o nome do filme: ")
        filmes[posicao - 1] = novoNomeFilme
        print("Filme substituído com sucesso!")
    else:
        print("Nenhum filme foi encontrado para o código informado.")


def removerFilme(filmes):
    posicao = int(input("Digite a posição do filme a ser removido: "))

    if posicao > 0 and posicao <= len(filmes):
        filmes.pop(posicao - 1)
        print("O filme foi removido")
    else:
        print("Nenhum filme foi encontrado para o código informado.")


def pesquisarFilme(filmes):
    posicao = int(input("Digite a posição do filme: "))

    if posicao > 0 and posicao <= len(filmes):
        filmePesquisado = filmes[posicao - 1]
        print("O filme pesquisado foi", filmePesquisado)
    else:
        print("Nenhum filme foi encontrado para o código informado.")


def adicionarFilme(filmes):
    novoFilme = input("Digite o nome do Filme: ")
    filmes.append(novoFilme)
    print("Filme adicionado com sucesso!")

def listarFilmes(filmes):
    if len(filmes) == 0:
        print("Nenhum filme foi encontrado.")
    else:
        print("Lista de Filmes")
        for filme in filmes:
            print("-", filme)
