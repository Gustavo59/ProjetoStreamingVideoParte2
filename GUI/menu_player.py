from LOGICA import player

def menu_assistir():
    print("\nAssistir Filme \n")
    titulo = input("Título do filme: ").title()
    cpf = int(input("CPF do usuário: "))
    player.assistir_filme(titulo, cpf)
    
def mostrar_menu():
    run_player = True
    menu = ("\n----------------\n"+
             "(1) Assistir Filme \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_player):
        print (menu)
        op = int(input("Digite sua escolha: "))
        if (op == 1):
            menu_assistir()
        elif (op == 0):
            run_player = False
