
import os

from api import *
from select_form import *
from pagina_usuario import *


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