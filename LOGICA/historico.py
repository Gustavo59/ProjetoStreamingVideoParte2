historico = []

def registrar_filme_assistido(titulo, cpf):    
    for h in historico:
        if h[1] == cpf:
            h[0].append(titulo)
            return
        
    historico.append([[],cpf])
    
    for h in historico:
        if h[1] == cpf:                
            h[0].append(titulo)
            return
               
def listar_filmes_assistidos(cpf):
    for h in historico:
        if cpf == h[1]:
            return h[0] 
        
    print("Nenhum filme assistido na conta informada ")
    return False



