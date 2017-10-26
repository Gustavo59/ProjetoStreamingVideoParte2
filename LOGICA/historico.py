import filme
import usuario

historico = []

def registrar_filme_assistido(titulo, cpf):
    for f in filme.filmes:
        if titulo == f[0]:
            for u in usuario.usuarios:
                if u[0] == cpf:
                    for h in historico:                        
                        if cpf == h[1]:
                            h[0].append(titulo)
                            return
    
            

    print("\nFilme ou Usuario Não Encontrado no Banco de Dados")

def listar_filmes_assistidos(cpf):
    for h in historico:
        if cpf == h[1]:
            return h[0]
    print("\nCPF não encontrado em nosso banco de dados ")

'''def iniciar_historico():
    for u in usuario.usuarios:
        historico.append([[], u[0]])'''



