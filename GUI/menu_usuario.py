from LOGICA import usuario

def imprimir_usuario(usuario):
    print ("CPF: ",  usuario[0])
    print ("Nome: ", usuario[1])
    print ("Email: ",  usuario[2])
    print("Senha: ", usuario[3])
    print ()

def menu_adicionar():
    print ("\nAdicionar Usuarios \n")
    cpf = int(input("CPF: "))
    nome = str (input("Nome: "))
    email = str(input("Email: "))
    senha = str(input("Senha: "))
    usuario.adicionar_usuario(cpf, nome, email, senha)

def menu_listar():
    print ("\nListar Usuarios \n")
    usuarios = usuario.listar_usuarios()
    for u in usuarios:
        imprimir_usuario(u)
