import os
import requests
import time

BASE_URL = "http://127.0.0.1:3000/api"

############### API ################################

def cadastrarUsuario(data):
    requests.post(BASE_URL + "/usuarios/", data)

def getUsuario(email):
    '''
        email = string
    '''
    return requests.get(BASE_URL + "/usuarios/?email=" + email)

def getUsuarioByID(idUsuario):
    #//Get user by id
    #//http://localhost:3000/api/usuarios/{idUsuario}
    return requests.get(BASE_URL + "/usuarios/"+ str(idUsuario))

def getPostagens(idUsuario):
    #//Get all posts from userX, where owner=X and id=X
    #//http://localhost:3000/api/usuarios/{idUsuario}/postagens/
    return requests.get(BASE_URL + "/usuarios/" + str(idUsuario) + "/postagens/")

def postPostagem(usuarioProprietario, idUsuarioDestino, data):
    # Post in PostagensUsuario
    # http://localhost:3000/api/usuarios/{usuarioProprietario}/postagens/{idUsuarioDestino}
    requests.post(BASE_URL + "/usuarios/" + str(usuarioProprietario) + "/postagens/" + str(idUsuarioDestino), data)

def cadastrarGrupo(data):
    # http://localhost:3000/api/grupos/
    requests.post(BASE_URL + "/grupos", data)

"""
def participacaoGrupo(data):
    requests.post(BASE_URL + "")
"""

def getAllGrupos(idUsuario):
    return requests.get(BASE_URL + "/grupos")

def getInfoUsers(parametro, busca):
    '''
    //http://localhost:3000/api/usuarios/?{parametro}={busca})
    '''
    return requests.get(BASE_URL + "/usuarios/?" + parametro + busca)

def amizadePost(idUsuario, data):
    pass
    #requests.post(BASE_URL + "/usuarios/" + str(idUsuario) + 1"/amizades/", data)


def getAmigos(idUsuario, data):
    return requests.post(BASE_URL + "/usuarios/" + str(idUsuario) + "/amizades/", data)


############### FIM API ########################################################



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
    bar = getUsuario(a)
    pagina_usuario(bar.json()[0])



def cadastrar():
    campos = {
        "nome": "",
        "email": "",
        "privacidade": "",
        "cidade":""
    }
    resultado = form(campos)
    
    # Mudando o valor da chave para a API
    resultado["nomeUsuario"] = resultado.pop("nome")
    
    cadastrarUsuario(resultado)
    landing_page()
    #print(resultado)
    #print(campos)


def fazer_postagens(idUsuario):
    os.system("clear")
    
    print("#"*50)
    print("\t Digite o conteudo da postagem:")
    print("#"*50, "\n\n")

    conteudo = input('>> ')
    
    os.system("clear")
    postPostagem
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

######################### AMIGOS ###############################################    

def ver_amigos(idUsuario):
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    print("#"*50)
    print("\t Amigos do: " + user_name)
    print("#"*50, "\n\n")

    data = {}

    amigos = getAmigos(idUsuario, data).json() 

    for amigo in amigos:
        print("#"*50)
        
        for key, value in amigo.items():
            print(key, ":",  value)
        """
        print("Usuario Proprietario:", getUsuarioByID(post["usuarioProprietario"]).json()[0]["nomeUsuario"])
        print("Usuario 2:", getUsuarioByID(post["idUsuario2"]).json()[0]["nomeUsuario"])
        print("Conteudo: \n", post["conteudo"])
        """
        print("#"*50, "\n\n")
        
    input()
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
    
    a = select("Amigos do Usuario: ", ["Ver Amigos", "Procurar pessoa"])
    
    if a == "1":
        ver_amigos(idUsuario)        
    elif a == "2":
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
        "foto": ""
    }
    resultado = form(campos)
    
    # Mudando o valor da chave para a API
    resultado["nomeGrupo"] = resultado.pop("Nome Grupo")
    resultado["descricaoGrupo"] = resultado.pop("Descrição Grupo")

    cadastrarGrupo(resultado)
    
    #print(resultado)
    #print(campos)
    pagina_usuario(idUsuario)

def ver_grupos(idUsuario):
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
def busca():
    #//http://localhost:3000/api/usuarios/?{parametro}={busca}

    parametro = input("Parametro: ")
    busca = input("Busca: ")

    print(getInfoUsers(parametro, busca))


################# FIM BUSCA ####################################################
    

################# CONFIGURAÇOES ################################################

def configuracoes(idUsuario):
    """
    Função criada para alterar os campos do usurário
    """
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    
    campos = ["Mudar dados:"]

    a = select("Pagina Usuario: " + user_name, campos)

    a = input(">> ")

############### FIM CONFIGURAÇOES ################################################



def pagina_usuario(user):
    os.system("clear")
    
    
    if type(user) == int:
        user = getUsuarioByID(user).json()[0]


    campos = ["Mural", "Amigos", "Grupos", "Busca", "Configurações"]

    a = select("Pagina Usuario: " + user["nomeUsuario"], campos)
    
    if a == "1":
        mural(user["idUsuario"])
    elif a == "2":
        amigos(user["idUsuario"])
    elif a == "3":
        grupos(user["idUsuario"])
    elif a == "4":
        busca()
    elif a == "5":
        configuracoes(user["idUsuario"])
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
    #pagina_usuario(1)
    #cadastrar()
    #print(getPostagens(1).json())
    #procurar_pessoa(1)

