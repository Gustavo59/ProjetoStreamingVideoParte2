from LOGICA import usuario
from LOGICA import filme
from LOGICA import historico

def assistir_filme(titulo, cpf):
    f = filme.buscar_filmes(titulo)
    u = usuario.buscar_usuario(cpf)

    if (f != None) and (u !=  None):
        historico.registrar_filme_assistido(f[0],u[0])
        print(" --------------------------------- ")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |      ------------------        |")
        print(" |     -        \         -       |")
        print(" |    -          \         -      |")
        print(" |    -          /         -      |")
        print(" |     -        /         -       |")
        print(" |      ------------------        |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" --------------------------------- ")
        print("\nVocê assistiu o filme",f[0],"!")
        print("Continue assitindo mais filmes de nosso catalogo!")
        return

    if (f == None) and (u != None):
        print("\nFilme Não Encontrado no Banco de Dados")
        return

    if (f != None) and (u == None):
        print("\nUsuario Não Encontrado no Banco de Dados")
        return

    print("\nFilme e Usuario Não Encontrado no Banco de Dados")
