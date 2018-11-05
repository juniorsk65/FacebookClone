import os 

from api import *
from pagina_usuario import *

def entrar():
    os.system("clear")
    print("#"*50)
    print("\tDigite o Email Cadastrado")
    print("#"*50, "\n\n")
    a = input(">> ")
    bar = getUsuario(a)
    pagina_usuario(bar.json()[0])
