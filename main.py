# La documentacion oficial
# https://docs.python.org/3/library/tk.html
# https://docs.python.org/es/3/library/tkinter.html
import json
from forms.Login import Login
from dashboard import Dashboard


# Primero leemos el fichero userLoged si existe un usuario conectado se inicia Dashboard 
usuarioConectado = False

# Oara detectar si hay algun usuario en el fichero de userloged y con eso pues abrir el login o la pantalla main
def hayUser():
    global usuarioConectado
    name = None
    with open("./userLoged.json","r") as file:
        datos = json.load(file)
        name = datos.get("name")
        print(name)
        # if datos.get("name") is None:
        #     usuarioConectado = False
        # else:       
        #     usuarioConectado = True

# Para abrir o el login o el "main"
def saberSiLogin():
    # Si no arranca la app es porque estoy haciendo cosas con el login
    # pon a mano el true dentro del siguiente if para que arranque
    if(usuarioConectado):
        Dashboard()
    else:
        Login()
        
        
hayUser()
saberSiLogin()



