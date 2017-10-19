filmes = []


def adicionar_filme(titulo, genero, ano):
    filme = [titulo, genero, ano]
    filmes.append(filme)


def listar_filmes():
    return filmes


def buscar_filmes(cod):
    for f in filmes:
        if (f[0] == cod):
            return f
    return None

def buscar_filmes_por_genero(genero):
    retorno = []
    for i in range(len(filmes)):
        for j in filmes[i]:
            if j == genero:
                retorno.append(filmes[i][0])
    if retorno:
        return retorno
    else:
        return


def remover_filme(titulo):
    for f in filmes:
        if (f[0] == titulo):
            filmes.remove(f)
            return True
    return False


def iniciar_filmes():
    adicionar_filme("Mulher Maravilha", "Ação", 2017)
    adicionar_filme("It - A Coisa", "Terror", 2017)
    adicionar_filme("Carros", "Aventura", 2006)
    adicionar_filme("Se Beber Não Case", "Comédia", 2009)

