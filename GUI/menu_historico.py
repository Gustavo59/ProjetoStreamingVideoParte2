from LOGICA import historico

def imprimir_filme(assistidos):
    for a in assistidos:
        print("Titulo:",a)

def menu_listar():
    print("\nListar Filmes Adicionados ao seu Histórico \n")
    cpf = int(input("Digite seu CPF: "))
    print()
    assistidos = historico.listar_filmes_assistidos(cpf)
    if (assistidos!= False):
        imprimir_filme(assistidos)

def mostrar_menu():
    run_historico = True
    menu = ("\n----------------\n"+
             "(1) Listar Filmes Assistidos \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_historico):
        print (menu)
        op = int(input("Digite sua escolha: "))
        if(op == 1):
            menu_listar()
        elif (op == 0):
            run_historico = False

