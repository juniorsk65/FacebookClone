import os
import sys
import time

from api import *


debug = open("debug.txt", "a")


def select(title, options):
    os.system("clear")
    print("#"*50)
    print("\t" + title)
    print("#"*50, "\n\n")
    for i in  range(len(options)):
        print(i+1, ' - ', options[i])
    user_input = input('>> ')
    return user_input

def form(inputs):
    accumulator = dict(inputs)
    for i in inputs: 
        os.system("clear")
        print("#"*50)
        print("\tDigite os dados abaixo:")
        for j in inputs:
            print(j, ":", accumulator[j])
        print("#"*50, "\n\n")
        accumulator[i] = input(str(i) + " >> ")

    os.system("clear")
    print("#"*50)
    print("\tConfirma a entrada com os campos abaixo?")
    for j in inputs:
        print(j, ":", accumulator[j])
    print("#"*50, "\n\n")
    confirm = input("[s/n] >> ")
    if confirm == 's':
        return accumulator
    else:
        return 0


def entrar():
    os.system("clear")
    print("#"*50)
    print("\tDigite o Email Cadastrado")
    print("#"*50, "\n\n")
    a = input(">> ")
    try:
        bar = getUsuario(a)
        pagina_usuario(bar.json()[0])
    except IndexError:
        print("Confira o email, talvez não possua conta")
    



def cadastrar():
    campos = {
        "nome": "",
        "email": "",
        "privacidade": "",
        "cidade":""
    }

    resultado = form(campos)
    
    
    if resultado == 0:
        input("Perfil não cadastrado, voltando para a pagina inicial")
        landing_page()
    else:        
        # Mudando o valor da chave para a API
        resultado["nomeUsuario"] = resultado.pop("nome")
        
        cadastrarUsuario(resultado)
        landing_page()

######################### MURAL ###############################################    


def fazer_postagens(idUsuario):
    os.system("clear")
    
    print("#"*50)
    print("\t Digite o conteudo da postagem:")
    print("#"*50, "\n\n")

    conteudo = input('>> ')
    
    os.system("clear")
    #postPostagem
    print("#"*50)
    print("\t O conteúdo: \n\n", conteudo, "\n\n está correto?[s/n]:")
    print("#"*50, "\n\n")

    confirmacao = input(">> ")
    
    data = {
        "usuarioProprietario": "",
        "idUsuario2": "",
        "conteudo":""
    }

    if confirmacao == 's' and len(conteudo) > 0:  
        print("A postagem será feita no próprio perfil")

        # Fazendo o JSON para a requisição da API
        data["usuarioProprietario"] = idUsuario
        data["idUsuario2"] = idUsuario
        data["conteudo"] = conteudo

        #print(data)
        postPostagem(idUsuario, idUsuario, data)
    input()
    pagina_usuario(idUsuario)
    

def ver_postagens(idUsuario):
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    print("#"*50)
    print("\tPostagens Usuario: " + user_name)
    print("#"*50, "\n\n")

    postagens = getPostagens(idUsuario).json() 
    
    if len(postagens) == 0:
        print("Não há posts neste mural.")
        input()
        pagina_usuario(idUsuario)

    for post in postagens:
        print("#"*50)
        """
        for key, value in post.items():
            print(key, ":",  value)
        """
        print("Usuario Proprietario:", getUsuarioByID(post["usuarioProprietario"]).json()[0]["nomeUsuario"])
        print("Usuario 2:", getUsuarioByID(post["idUsuario2"]).json()[0]["nomeUsuario"])
        print("Conteudo: \n", post["conteudo"])
        print("#"*50, "\n\n")
    
    input()
    pagina_usuario(idUsuario)


def mural(idUsuario):
    '''
        idUsuario = int
    '''
    os.system("clear")
    
    a = select("Mural Usuario: ", ["Ver Postagens", "Fazer Postagens"])
    
    if a == "1":
        ver_postagens(idUsuario)
    elif a == "2":
        fazer_postagens(idUsuario)
    else:
        input("Digitou errado, retornando para pagina principal")
        pagina_usuario(idUsuario)

###################### END MURAL ###############################################    


######################### AMIGOS ###############################################    

def ver_amigos(idUsuario):
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    print("#"*50)
    print("\t Amigos do: " + user_name)
    print("#"*50, "\n\n")

    data = {}

    amigos = getAmigos(idUsuario, data).json()
    
    id_amigos = []
    numero = 1

    for amigo in amigos:
        print("#"*15, numero ,"#"*32)
        numero = numero + 1
        id_amigos.append(amigo["idUsuario"])

        print("Nome Usuario:", amigo["nomeUsuario"])
        print("Email:", amigo["email"])
        print("#"*50, "\n\n")

    
    entrada = input("Você deseja visualizar o perfil de algum amigo?[s/n] ")
    print(entrada, file=debug)

    print(entrada, file=sys.stderr)

    if entrada == "s":
        numero_amigo_aceitado = int(input("Qual amigo deseja visualizar?[Numero] "))
        print(numero_amigo_aceitado, id_amigos[numero_amigo_aceitado - 1])
        input()
    elif entrada == "n":
        input("Voltando para pagina inicial")
        pagina_usuario(idUsuario)
        input()
    else:
        input("Entrada inválida")
        pagina_usuario(idUsuario)
    

def ver_amigos_pendentes(idUsuario):
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    print("#"*50)
    print("\t Amigos do: " + user_name)
    print("#"*50, "\n\n")

    data = {}

    amigos = getAmigosPendentes(idUsuario, data).json()
    #print(amigos)

    if len(amigos) == 0:
        print("Não há amigos pendentes.")
        input()
        pagina_usuario(idUsuario)


    amigos_pendentes = []
    numero = 1

    for amigo in amigos:
        print("#"*15, numero ,"#"*32)
        numero = numero + 1
        amigos_pendentes.append(amigo["idUsuario"])

        print("Nome Usuario:", amigo["nomeUsuario"])
        print("Email:", amigo["email"])
        print("#"*50, "\n\n")
    
    entrada = input("Você deseja aceitar algum amigo pendente?[s/n]")
    
    if entrada == "s":
        numero_amigo_aceitado = int(input("Qual amigo deseja aceitar? [Numero] "))
        print(numero_amigo_aceitado)
        print(amigos_pendentes[numero_amigo_aceitado - 1])
        data = {
            "status":1
        }    
        try:
            updateAmizade(idUsuario, amigos_pendentes[numero_amigo_aceitado-1], data)
        except:
            print("Não foi possivel realizar a mudança")
        input()
        pagina_usuario(idUsuario)
    elif entrada == "n":
        input("Voltando para pagina inicial")
        pagina_usuario(idUsuario)
        input()
    else:
        input("Entrada inválida")
        pagina_usuario(idUsuario)
    

def procurar_pessoa(idUsuario):
    #pass
    os.system("clear")
    print("#"*50)
    print("\t Digite o email do amigo para procurar:")
    print("#"*50, "\n\n")

    email = input(">> ")
    try:
        print(getUsuario(email).json()[0])
    except:
        input("Email não encontrado")
        pagina_usuario(idUsuario)

    # Considerando que 0 é o mais permissivo possivel
    if getUsuario(email).json()[0]["privacidade"] != 0:
        print("Usuario não possui perfil público")

    amizade = {
        "idUsuario1": idUsuario,
        "idUsuario2": getUsuario(email).json()[0]["idUsuario"],
        "bloqueio": 0,
        "status": 0
        }

    print(amizade)
    amizadePost(idUsuario, amizade)
    input()
    pagina_usuario(idUsuario)
    

def amigos(idUsuario):
    """
    Pagina amigos
    """
    os.system("clear")

    escolhas = ["Ver Amigos", "Ver Amigos Pendentes", "Procurar pessoa"]
    
    a = select("Amigos do Usuario: ", escolhas)
    
    if a == "1":
        ver_amigos(idUsuario)        
    elif a == "2":
        ver_amigos_pendentes(idUsuario)
    elif a == "3":
        procurar_pessoa(idUsuario)        
    else:
        input("Digitou errado, retornando para pagina principal")
        pagina_usuario(idUsuario)

##################### FIM AMIGOS ###############################################

######################## GRUPOS ################################################


def fazer_grupo(idUsuario):
    campos = {
        "Nome Grupo": "",
        "Descrição Grupo": "",
        "foto": "",
    }
    resultado = form(campos)
    
    # Mudando o valor da chave para a API
    resultado["nomeGrupo"] = resultado.pop("Nome Grupo")
    resultado["descricaoGrupo"] = resultado.pop("Descrição Grupo")
    
    
    # Novos campos para no momento da criação do grupo, crie um relacionamento
    # do tipo Admin com o usuário que criou. 

    # Id do usuário que está relacionada ao grupo
    resultado["Usuario_idUsuario"] = str(idUsuario)
    
    # Se um usuário criou o grupo, ele será o admin (flag 1 para admin)
    resultado["Administrador"] = str(1)
    
    # Sempre o primeiro usuário será o melhor
    resultado["Participacao"] = str(1)
    

    cadastrarGrupo(resultado)
    
    #print(resultado)
    #print(campos)
    #input()
    pagina_usuario(idUsuario)

def ver_grupos(idUsuario):
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    print("#"*50)
    print("\t Amigos do: " + user_name)
    print("#"*50, "\n\n")

    data = {}

    amigos = getAmigosPendentes(idUsuario, data).json()
    #print(amigos)

    if len(amigos) == 0:
        print("Não há amigos pendentes.")
        input()
        pagina_usuario(idUsuario)


    amigos_pendentes = []
    numero = 1

    for amigo in amigos:
        print("#"*15, numero ,"#"*32)
        numero = numero + 1
        amigos_pendentes.append(amigo["idUsuario"])

        print("Nome Usuario:", amigo["nomeUsuario"])
        print("Email:", amigo["email"])
        print("#"*50, "\n\n")
    
    entrada = input("Você deseja aceitar algum amigo pendente?[s/n]")
    
    if entrada == "s":
        numero_amigo_aceitado = int(input("Qual grupo deseja entrar aceitar? [Numero] "))
        print(numero_amigo_aceitado)
        print(amigos_pendentes[numero_amigo_aceitado - 1])
        data = {
            "status":1
        }    
        try:
            updateAmizade(idUsuario, amigos_pendentes[numero_amigo_aceitado-1], data)
        except:
            print("Não foi possivel realizar a mudança")
        input()
        pagina_usuario(idUsuario)
    elif entrada == "n":
        input("Voltando para pagina inicial")
        pagina_usuario(idUsuario)
        input()
    else:
        input("Entrada inválida")
        pagina_usuario(idUsuario)

    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    print("#"*50)
    print("\tGrupos Usuario: " + user_name)
    print("#"*50, "\n\n")

    grupos = getAllGrupos(idUsuario).json() 


    for grupo in grupos:
        print("#"*50)
        
        for key, value in grupo.items():
            print(key, ":",  value)
        """
        print("Usuario Proprietario:", getUsuarioByID(post["usuarioProprietario"]).json()[0]["nomeUsuario"])
        print("Usuario 2:", getUsuarioByID(post["idUsuario2"]).json()[0]["nomeUsuario"])
        print("Conteudo: \n", post["conteudo"])
        """
        print("#"*50, "\n\n")
    
    input()
    pagina_usuario(idUsuario)

    


def grupos(idUsuario):
    os.system("clear")
    
    a = select("Grupos: ", ["Ver Grupos", "Fazer Grupos"])
    
    if a == "1":
        ver_grupos(idUsuario)
    elif a == "2":
        fazer_grupo(idUsuario)
    else:
        input("Digitou errado, retornando para pagina principal")
        pagina_usuario(idUsuario)

################# FIM GRUPOS ###################################################


################# BUSCA ########################################################
def busca(idUsuario):
    #//http://localhost:3000/api/usuarios/?{parametro}={busca}
    os.system("clear")

    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]

    print("#"*50)
    print("\tBusca Usuario: " + user_name)
    print("#"*50, "\n\n")

    parametro = input("Parametro: ")
    busca = input("Busca: ")

    print(getInfoUsers(parametro, busca))


################# FIM BUSCA ####################################################

################# CONFIGURAÇOES ################################################

def recadastrar(idUsuario):
    os.system("clear")

    campos = {
        "nome": "",
        "privacidade": "",
        "cidade":""
    }
    resultado = form(campos)
    
    # Mudando o valor da chave para a API
    resultado["nomeUsuario"] = resultado.pop("nome")
    
    updateUsuario(idUsuario, resultado)

    pagina_usuario(idUsuario)

    

def apagar_perfil(idUsuario):

    os.system("clear")

    a = select("Você tem certeza que deseja apagar a sua conta?", ["Sim", "Não"])

    if a == "1":
        email = input("Confirme o seu email: ")
        if email == getUsuarioByID(idUsuario).json()[0]["email"]:
            deleteUsuario(idUsuario)
            print("Dados e postagens apagadas. Até mais.")
            input()
        else:
            input("Email incorreto, voltando para a pagina principal.")
            pagina_usuario(idUsuario)
    elif a == "2":
        input("Cancelamento cancelado, voltando para a pagina principal.")
        pagina_usuario(idUsuario)
    else:
        input("Dígito errado, retornando para a pagina principal.")
        pagina_usuario(idUsuario)
        

    
def configuracoes(idUsuario):
    """
    Função criada para alterar os campos do usurário
    """
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    
    campos = ["Mudar dados", "Apagar perfil"]

    a = select("Pagina Usuario: " + user_name, campos)

    if a == "1":
        recadastrar(idUsuario)
    elif a == "2":
        apagar_perfil(idUsuario)
    else:
        input("Digitou errado, retornando para pagina principal")
        pagina_usuario(idUsuario)


############### FIM CONFIGURAÇOES ################################################


def sair():
    os.system("clear")

    print("Software encerrado")



def pagina_usuario(user):
    os.system("clear")
    
    
    if type(user) == int:
        user = getUsuarioByID(user).json()[0]


    campos = ["Mural", "Amigos", "Grupos", "Busca", "Configurações", "Sair"]

    a = select("Pagina Usuario: " + user["nomeUsuario"], campos)
    
    if a == "1":
        mural(user["idUsuario"])
    elif a == "2":
        amigos(user["idUsuario"])
    elif a == "3":
        grupos(user["idUsuario"])
    elif a == "4":
        busca(user["idUsuario"])
    elif a == "5":
        configuracoes(user["idUsuario"])
    elif a == "6":
        sair()
    else:
        input("Digitou errado, retornando para pagina principal")
        pagina_usuario(user)


def landing_page():
    a = select("Bem vindo ao clone do Facebook", ["Entrar", "Cadastrar"])
    if a == "1":
        entrar()
    elif a == "2":
        cadastrar()
    else:
        input("Digitou errado, retornando para pagina principal")
        landing_page()

if __name__ == "__main__":
    landing_page()
    
    # Para debugar

    #pagina_usuario(9)
    #cadastrar()
    #print(getPostagens(1).json())
    #procurar_pessoa(9)

