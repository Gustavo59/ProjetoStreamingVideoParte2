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
        if (f[0] == cod):
            return f
    return None


def remover_filme(cod):
    for f in filmes:
        if (f[0] == cod):
            filmes.remove(f)
            return True
    return False


def iniciar_filmes():
    adicionar_filme("Charles", "charles@gmail.com", "charles123")
    adicionar_filme("Gustavo", "gustavo@gmail.com", "gustavo845")
    adicionar_filme("André", "andré@gmail.com", "andre224")
    adicionar_filme("Gabriel", "gabriel@gmail.com", "gabriel448")

