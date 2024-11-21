# La documentacion oficial
# https://docs.python.org/3/library/tk.html
# https://docs.python.org/es/3/library/tkinter.html

from forms.Login import Login
from Dashboard import Dashboard
# Primero leemos el fichero userLoged si existe un usuario conectado se inicia Dashboard 
usuarioConectado = False

if(usuarioConectado):
    Dashboard()
else:
    Login()

