from LOGICA import interesse

def imprimir_filme(assistidos):
    for a in assistidos:
        print("Titulo:",a)    

def menu_adicionar():
    print("\nAdicionar Filme a sua Lista de Interesse\n")
    cpf = int(input("CPF do usuário: "))
    titulo = input("Título do filme: ").title()    
    interesse.adicionar_filme(titulo, cpf)

def menu_listar():
    print("\nListar Filmes Adicionados a sua Lista de Interesse \n")
    cpf = int(input("Digite seu CPF: "))
    print()
    assistidos = interesse.listar_interesses(cpf)
    imprimir_filme(assistidos)

def menu_remover():
    print ("\nRemover Filme \n")
    cpf = int(input("Digite seu CPF: "))
    titulo = input("Título do filme: ").title()
    print()
    f = interesse.remover_interesse(titulo,cpf)
    
def mostrar_menu():
    run_interesse = True
    menu = ("\n----------------\n"+
             "(1) Adicionar Filme a sua Lista de Interesse \n" +
             "(2) Listar Filmes da Lista de Interesse \n" +
             "(3) Remover Filme da Lista de Interesse \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_interesse):
        print (menu)
        op = int(input("Digite sua escolha: "))
        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):
            menu_remover()
        elif (op == 0):
            run_interesse = False

