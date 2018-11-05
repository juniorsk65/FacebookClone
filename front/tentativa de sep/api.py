import requests


############### API ################################
BASE_URL = "http://127.0.0.1:3000/api"
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
