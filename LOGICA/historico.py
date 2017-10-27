from LOGICA import usuario
from LOGICA import filme


historico = []

def registrar_filme_assistido(titulo, cpf):
    f = filme.buscar_filmes(titulo)
    u = usuario.buscar_usuario(cpf)

    if (f != None) and (u !=  None):
        for h in historico:
            if h[1] == cpf:
                h[0].append(titulo)
                return
        historico.append([[],cpf])
        historico[0].append(titulo)
            
    
            

    print("\nFilme ou Usuario Não Encontrado no Banco de Dados")

def listar_filmes_assistidos(cpf):
    for h in historico:
        if cpf == h[1]:
            return h[0]
    print("\nCPF não encontrado em nosso banco de dados ")

'''def iniciar_historico():
    for u in usuario.usuarios:
        historico.append([[], u[0]])'''



