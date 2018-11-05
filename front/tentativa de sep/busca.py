
from api import *

def busca():
    #//http://localhost:3000/api/usuarios/?{parametro}={busca}

    parametro = input("Parametro: ")
    busca = input("Busca: ")

    print(getInfoUsers(parametro, busca))
