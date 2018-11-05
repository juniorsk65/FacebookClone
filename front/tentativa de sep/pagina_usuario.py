
import os

from mural import *
from amigos import *
from grupos import * 
from busca import *
from configuracoes import *

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