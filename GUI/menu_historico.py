from LOGICA import historico


def imprimir_filme(filme):
    for f in filme:
        print("Título:",f)

def menu_registrar():
    print("\nAdicionar filme assistido no seu historico \n")
    titulo = input("Título do filme: ").title()
    cpf = int(input("CPF do usuário: "))
    historico.registrar_filme_assistido(titulo, cpf)

def menu_listar():
    print("\nListar Filmes adicionados ao histórico \n")
    cpf = int(input("Pro favor digite seu CPF "))
    assistidos = historico.listar_filmes_assistidos(cpf)
    for a in assistidos:
        imprimir_filme(a)

   

def mostrar_menu():
    run_historico = True
    menu = ("\n----------------\n"+
             "(1) Registrar um filme assistido \n" +
             "(2) Listar Filmes assistidos \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_historico):
        print (menu)
        op = int(input("Digite sua escolha: "))
        if (op == 1):
            menu_registrar()
        elif(op == 2):
            menu_listar()
        elif (op == 0):
            run_historico = False

