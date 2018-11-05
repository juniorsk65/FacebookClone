import os 
 
from api import * 
from select_form import *
from pagina_usuario import *


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