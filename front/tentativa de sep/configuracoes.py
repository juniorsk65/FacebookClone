
import os


from api import *
from select_form import *

def configuracoes(idUsuario):
    """
    Função criada para alterar os campos do usurário
    """
    os.system("clear")
    
    user_name = getUsuarioByID(idUsuario).json()[0]["nomeUsuario"]
    
    campos = ["Mudar dados:"]

    a = select("Pagina Usuario: " + user_name, campos)

    a = input(">> ")