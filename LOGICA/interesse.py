from LOGICA import usuario
from LOGICA import filme

interesses = []

def adicionar_filme(titulo, cpf):
    f = filme.buscar_filmes(titulo)
    u = usuario.buscar_usuario(cpf)
    
    if (f != None) and (u !=  None):
        for i in interesses:
            if i[1] == cpf:
                i[0].append(titulo)
                print("\nO filme",titulo,"foi adicionado a sua lista de interesses")
                return
            
        interesses.append([[],cpf])
        
        for i in interesses:
            if i[1] == cpf:                
                i[0].append(titulo)
                print("\nO filme",titulo,"foi adicionado a sua lista de interesses")
                return
            
    if (f == None) and (u != None):
        print("\nFilme Não Encontrado no Banco de Dados")
        return

    if (f != None) and (u == None):
        print("\nUsuario Não Encontrado no Banco de Dados")
        return

    print("\nFilme e Usuario Não Encontrados no Banco de Dados")

def listar_interesses(cpf):
    for i in interesses:
        if cpf == i[1]:
            return i[0]
        
    print("CPF não encontrado em nosso banco de dados ")
    return []

def remover_interesse(titulo,cpf):
    for i in interesses:
        if (i[1] == cpf):
            i[0].remove(titulo)
            print("O filme",titulo,"foi removido da sua lista de interesses")
            return
    
    f = filme.buscar_filmes(titulo)
    u = usuario.buscar_usuario(cpf)

    if (f == None) and (u != None):
        print("Filme Não Encontrado no Banco de Dados")
        return

    if (f != None) and (u == None):
        print("Usuario Não Encontrado no Banco de Dados")
        return

    print("Filme e Usuario Não Encontrados no Banco de Dados")


