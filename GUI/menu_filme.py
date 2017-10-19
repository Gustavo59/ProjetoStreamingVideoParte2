from LOGICA import filme


def imprimir_filme(filme):
    print("Título:", filme[0])
    print("Gênero:", filme[1])
    print("Ano:", filme[2])
    print()

def menu_adicionar():
    print("\nAdicionar Filmes \n")
    titulo = input("Título do filme: ").title()
    genero = input("Gênero do filme: ").title()
    ano = int(input("Ano de lançamento do filme: "))
    filme.adicionar_filme(titulo, genero, ano)

def menu_listar():
    print("\nListar Filmes \n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

   
def menu_buscar():
    print ("\nBuscar Filme por Nome: \n")
    nome = input("Nome do filme: ").title()
    print()
    f = filme.buscar_filmes(nome)
    if (f == None):
        print ("Filme não encontrado no catálogo ")
    else:
        imprimir_filme(f)


def menu_buscar_por_genero():
    print("\nBuscar Filme por Gênero \n")
    genero = input("Digite o gênero desejado: ").title()
    print("\nFilmes de",genero,": \n")
    g = filme.buscar_filmes_por_genero(genero)
    for i in range(len(g)):
        print('Título:',g[i],'\n')
        

def menu_remover():
    print ("\nRemover Filme \n")
    titulo = input("Título do filme: ").title()
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

