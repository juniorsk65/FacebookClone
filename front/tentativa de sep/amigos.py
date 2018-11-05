
import os

from pagina_usuario import *
from api import *
from select_form import *


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