usuarios = []

def adicionar_usuario(cpf, nome, email, senha):    
    usuario = [cpf, nome, email, senha]
    usuarios.append(usuario)
    
def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            return u
    return None
        
def remover_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            usuarios.remove(u)
            return True
    return False        
    
def iniciar_usuarios():
    adicionar_usuario(1, "Charles", "charles@gmail.com", "charles123")
    adicionar_usuario(2, "Gustavo", "gustavo@gmail.com", "gustavo845")
    adicionar_usuario(3, "André", "andré@gmail.com", "andre224")
    adicionar_usuario(4, "Gabriel", "gabriel@gmail.com", "gabriel448")
    
