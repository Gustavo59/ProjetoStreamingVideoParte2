from LOGICA import filme

def imprimir_filme(filme):
    print("Título: ", filme[0])
    print("Gênero: ", filme[1])
    print("Ano: ", filme[2])


def menu_adicionar():
    print("\nAdicionar Filmes \n")
    titulo = input("Título do filme: ")
    genero = input("Gênero do filme: ")
    ano = int(input("Ano de lançamento do filme "))

def menu_listar():
    print("\Listar filmes ")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)


    
