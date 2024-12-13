import customtkinter as ctk
from dashboard import Dashboard

import mariadb
import sys
import json

# Variables Globales
nombreLogin = ""
pwdLogin = ""
entryLoginNombre = None
entryLoginPwd = None 

def FormLogin(root, contenedorDeFormulario):
    global entryLoginNombre
    global entryLoginPwd
    
    formularioLogin = ctk.CTkFrame(
        contenedorDeFormulario, 
        fg_color="#f7f7f7", 
        width=450,
        height=450
    )
    formularioLogin.pack_propagate(False)
    formularioLogin.place(relx=0.5, rely=0.5, anchor="center")

    lbTituloFormLogin = ctk.CTkLabel(
        formularioLogin, 
        text="Login", 
        text_color="#000", 
        font=("Arial", 32, "bold")
    )
    lbTituloFormLogin.pack(side="top", fill="x", pady=20)

    lbLoginUsuario = ctk.CTkLabel(
        formularioLogin, 
        text="Usuario", 
        text_color="#000", 
        font=("Arial", 16), 
        anchor="w", 
        fg_color="#f7f7f7"
    )
    lbLoginUsuario.pack(side="top", fill="x", padx=(5,0))

    entryLoginNombre = ctk.CTkEntry(
        formularioLogin,
        placeholder_text="Ingresa tu usuario",
        font=("Arial", 14), 
        height=50, 
        text_color="black", 
        fg_color="#EBEBEB", 
        corner_radius=10, 
        border_color="#f7f7f7"
    )
    entryLoginNombre.pack(side="top", fill="x", pady=(0,20))    

    lbLoginPwd = ctk.CTkLabel(
        formularioLogin, 
        text="Contraseña", 
        text_color="#000", 
        font=("Arial", 16), 
        anchor="w", 
        fg_color="#f7f7f7"
    )
    lbLoginPwd.pack(side="top", fill="x", pady=(5,0))

    entryLoginPwd = ctk.CTkEntry(
        formularioLogin, 
        show="*", 
        placeholder_text="Ingresa tu contraseña", 
        font=("Arial", 14),
        height=50, 
        text_color="black", 
        fg_color=("black", "#EBEBEB"), 
        corner_radius=10, 
        border_color="#f7f7f7"
    )
    entryLoginPwd.pack(side="top", fill="x", pady=(0,40))

    btnValidarUsuario = ctk.CTkButton(
        formularioLogin, 
        text="Iniciar Sesión", 
        font=("Arial", 20, "bold"), 
        width=200, 
        height=50, 
        anchor="center", 
        text_color="black",
        fg_color="#FFCC00", 
        hover_color="#ECBD00", 
        corner_radius=10, 
        command=lambda: conexionLogin(root)
    )
    btnValidarUsuario.pack()
    
    
def conexionLogin(root):
    entryLoginNombre  # Usa la variable global
    entryLoginPwd
    # Obtén el valor introducido en entryLoginNombre
    nombreLogin = entryLoginNombre.get()
    pwdLogin = entryLoginPwd.get()
    print(f"Nombre de Usuario: {nombreLogin}")
    print(f"PWD de Usuario: {pwdLogin}")
    
    # La conexion a la base de datos
    try:
        conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="pyolingo"
        )
    except mariadb.Error as e:
        print("Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
        

    # Get Cursor
    cur = conn.cursor()
    try:
        # EL metodo que ejecuta las querys
        cur.execute(
            f"SELECT * FROM usuario Where nombre = '{nombreLogin}' AND pwd = '{pwdLogin}'"
        )
        reader = cur.fetchone()
        
        # El registro de login
        if reader is None:
            print("nada")
        else:
            
            niveles = json.loads(reader[4])
            user_data = {
                "name":reader[1],
                "lvl": niveles
            }
            user_data_json = json.dumps(user_data)
            
            # La escritura del fichero
            with open("./userLoged.json","w") as file:
                try:
                    json.dump(user_data_json,file,indent=4)
                except:
                    print("Error al insertar datos")
            
            CerrarAplicacion(root)
            
        
    except:
        print("User not found (error en la query)")
        
    cur.close()



def CerrarAplicacion(root):
    root.destroy()
    Dashboard()