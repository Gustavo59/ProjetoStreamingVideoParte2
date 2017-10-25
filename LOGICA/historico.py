from LOGICA import filme
from LOGICA import usuario

historico = []

def registrar_filme_assistido(titulo, cpf):
    for f in filme.filmes:
        if titulo == f[0]:
            for u in usuario.usuarios:
                if u[0] == cpf:
                    print(historico)
                    for h in historico:                        
                        if cpf == h[1]:
                            print(h[1])
                            h[0].append(titulo)
                            return
                        else:
                            historico.append([[titulo], cpf])
                            return
                    
                '''else:
                    print("Usuário não encontrado na base de dados")
                    return'''
        
    print("Filme ou Usuario não encontrado na base de dados ")
    return
            
            


def listar_filmes_assistidos(cpf):
    for h in historico:
        if cpf == h[1]:
            return h[0]
        else:
            print("CPF não encontrado em nosso banco de dados ")

def iniciar_historico():
    for u in usuario.usuarios:
        historico.append([[], u[0]])



