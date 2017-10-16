from LOGICA import filme


def imprimir_filme(filme):
    print("Título: ", filme[0])
    print("Gênero: ", filme[1])
    print("Ano: ", filme[2])
    print()

def menu_adicionar():
    print("\nAdicionar Filmes \n")
    titulo = input("Título do filme: ")
    titulo = titulo.lower()
    genero = input("Gênero do filme: ")
    genero = genero.lower()
    ano = int(input("Ano de lançamento do filme "))
    filme.adicionar_filme(titulo, genero, ano)

def menu_listar():
    print("\nListar filmes ")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

   
def menu_buscar():
    print ("\nBuscar Filme por nome: \n")
    nome = input("Nome do filme: ")
    print()
    f = filme.buscar_filmes(nome)
    if (f == None):
        print ("Filme não encontrado no catálogo ")
    else:
        imprimir_filme(f)


def menu_buscar_por_genero():
    print("Buscar filme por gênero ")
    genero = input("Digite o gênero desejado: ")
    print()
    g = filme.buscar_filmes_por_genero(genero)
    if(g == None):
        print("Nenhum filme do gênero desejado foi encontrado ")
    else:
        
        imprimir_filme(g)

def menu_remover():
    print ("\nRemover Filme \n")
    titulo = input("Título do filme: ")
    print()
    f = filme.remover_filme(titulo)
    if (f == False):
        print ("Filme não encontrado")
    else:
        print ("Filme removido")


def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Filme \n" +
             "(2) Listar Filmes \n" +
             "(3) Buscar Filme \n" +
             "(4) Buscar Filmes por Gênero \n" +
             "(5) Remover Filme \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_filme):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif(op == 4):       
            menu_buscar_por_genero()
        elif (op == 5):
            menu_remover()
        elif (op == 0):
            run_filme = False

