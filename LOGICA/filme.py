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
    for f in filmes:
        if (f[1] == genero):
            return f
    return None


def remover_filme(titulo):
    for f in filmes:
        if (f[0] == titulo):
            filmes.remove(f)
            return True
    return False


def iniciar_filmes():
    adicionar_filme("mulher maravilha", "acao", 2017)
    adicionar_filme("it - a coisa", "terror", 2017)
    adicionar_filme("carros", "aventura", 2006)
    adicionar_filme("se beber não case", "comedia", 2009)

