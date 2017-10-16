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

   
def menu_buscar():
    print ("\nBuscar Filme por Código \n")
    cod = int(input("Código: "))
    print()
    f = filme.buscar_filme(cod)
    if (f == None):
        print ("Filme não encontrado no catálogo ")
    else:
        imprimir_filme(f)


def menu_remover():
    print ("\nRemover Filme \n")
    cod = int(input("Código: "))
    print()
    f = filme.remover_filme(cod)
    if (f == False):
        print ("Filme não encontrado")
    else:
        print ("Filme removido")
