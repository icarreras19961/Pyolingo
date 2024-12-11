# La documentacion oficial
# https://docs.python.org/3/library/tk.html
# https://docs.python.org/es/3/library/tkinter.html
import json
from forms.Login import Login
from dashboard import Dashboard
import os

# Primero leemos el fichero userLoged si existe un usuario conectado se inicia Dashboard 
usuarioConectado = False

# Oara detectar si hay algun usuario en el fichero de userloged y con eso pues abrir el login o la pantalla main
def hayUser():
    global usuarioConectado
    
    if not(os.stat("./userLoged.json").st_size == 0):
        with open("./userLoged.json","r") as file:
            data = json.load(file)
        json_object = json.loads(data)
        if((not json_object["name"] is None) and (not len(json_object["name"]) == 0)):
            Dashboard()
        else:
            Login
    else:
        Login()

hayUser()