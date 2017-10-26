from LOGICA import filme
from GUI import  menu_filme

from LOGICA import usuario
from GUI import  menu_usuario

from LOGICA import historico
from GUI import  menu_historico

def inicializar_dados():
    usuario.iniciar_usuarios()
    filme.iniciar_filmes()
    #historico.iniciar_historico()
  
def exibir_menu_principal():
    run_menu = True

    inicializar_dados()
    
    menu = ("\n----------------\n"+
             "(1) Menu Usuário \n" +
             "(2) Menu Filme \n" +
             "(3) Menu Historico \n" +
             "(0) Sair\n"+
            "----------------")
    
    while(run_menu):
        print (menu)
        
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_usuario.mostrar_menu()
        elif(op == 2):            
            menu_filme.mostrar_menu()
        elif(op == 3):            
            menu_historico.mostrar_menu()
        elif (op == 0):
            print ("Saindo do programa...")
            run_menu = False
        else:
            print ("Valor invalido")
