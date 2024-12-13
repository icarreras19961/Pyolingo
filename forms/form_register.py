import customtkinter as ctk
from dashboard import Dashboard

import json
import mariadb
import sys

# Las variables globales que necesito para hacer el insert
entryRegisterUsuario = None
entryRegisterPwd = None
entryRegisterEmail = None

def FormRegister(root, contenedorDeFormulario):
    global entryRegisterUsuario
    global entryRegisterPwd
    global entryRegisterEmail

    formularioRegister = ctk.CTkFrame(
        contenedorDeFormulario, 
        fg_color="#f7f7f7", 
        width=450,
        height=450
    )
    formularioRegister.pack_propagate(False)
    formularioRegister.place(relx=0.5, rely=0.5, anchor="center")


    # Titulo
    lbTituloFormRegister = ctk.CTkLabel(
        formularioRegister, 
        text="Register", 
        text_color="#000", 
        font=("Arial", 32, "bold")
    )
    lbTituloFormRegister.pack(side="top", fill="x", pady=20)


    # ----------------- Nombre Usuario----------------------
    lbRegisterUsuario = ctk.CTkLabel(
        formularioRegister, 
        text="Usuario", 
        text_color="#000", 
        font=("Arial", 16), 
        anchor="w", 
        fg_color="#f7f7f7"
    )
    lbRegisterUsuario.pack(side="top", fill="x", padx=(5,0))

    entryRegisterUsuario = ctk.CTkEntry(
        formularioRegister,
        placeholder_text="Ingresa tu usuario",
        font=("Arial", 14), 
        height=50, 
        text_color="black", 
        fg_color="#EBEBEB", 
        corner_radius=10, 
        border_color="#f7f7f7"
    )
    entryRegisterUsuario.pack(side="top", fill="x", pady=(0,20))
    
    # --------------------- Correo ------------------------
    lbRegisterEmail = ctk.CTkLabel(
        formularioRegister, 
        text="Email", 
        text_color="#000", 
        font=("Arial", 16), 
        anchor="w", 
        fg_color="#f7f7f7"
    )
    lbRegisterEmail.pack(side="top", fill="x", padx=(5,0))

    entryRegisterEmail = ctk.CTkEntry(
        formularioRegister,
        placeholder_text="Ingresa tu email",
        font=("Arial", 14), 
        height=50, 
        text_color="black", 
        fg_color="#EBEBEB", 
        corner_radius=10, 
        border_color="#f7f7f7"
    )
    entryRegisterEmail.pack(side="top", fill="x", pady=(0,20))       

    # --------------------- Contraseña -------------------------
    lbRegisterPwd = ctk.CTkLabel(
        formularioRegister, 
        text="Contraseña", 
        text_color="#000", 
        font=("Arial", 16), 
        anchor="w", 
        fg_color="#f7f7f7"
    )
    lbRegisterPwd.pack(side="top", fill="x", padx=(5,0))

    entryRegisterPwd = ctk.CTkEntry(
        formularioRegister, 
        show="*", 
        placeholder_text="Ingresa tu contraseña", 
        font=("Arial", 14),
        height=50, 
        text_color="black", 
        fg_color=("black", "#EBEBEB"), 
        corner_radius=10, 
        border_color="#f7f7f7"
    )
    entryRegisterPwd.pack(side="top", fill="x", pady=(0,40))

    # ----------------- Registrar Usuario --------------------------
    btnRegistrarUsuario = ctk.CTkButton(
        formularioRegister, 
        text="Registrarse", 
        font=("Arial", 20, "bold"), 
        width=200, 
        height=50, 
        anchor="center", 
        text_color="black",
        fg_color="#FFCC00", 
        hover_color="#ECBD00", 
        corner_radius=10, 
        command=lambda: CerrarAplicacion(root)
    )
    btnRegistrarUsuario.pack()

def CerrarAplicacion(root):
    nombreRegister = entryRegisterUsuario.get()
    pwdRegister = entryRegisterPwd.get()
    emailRegister = entryRegisterEmail.get()
    jsonLvl= {
            "lvl": [
                {
                    "writing": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                },
                {
                    "reading": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                },
                {
                    "listening": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                },
                {
                    "speaking": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                }
            ]
        }
    print(nombreRegister +" "+ pwdRegister+" "+emailRegister+" "+json.dumps(jsonLvl))
    # INSERT en la base de datos y Guardar el usuario que se acaba de resistrar userLoged
    # Destruimos todo la aplicacion de Login y iniciamos Dashboard
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
    cur = conn.cursor()
    try:
        # La query de insert
        query = f"INSERT INTO usuario(id,nombre,pwd,email,lvlComplete)VALUES (DEFAULT,'{nombreRegister}','{pwdRegister}','{emailRegister}','{json.dumps(jsonLvl)}')"
        cur.execute(query)
        # Hace falta hacer el comit para que la base de datos se actualize
        conn.commit()
        print("Un exito")
        user_registered = {
            "name": nombreRegister,
            "lvl": [
                {
                    "writing": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                },
                {
                    "reading": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                },
                {
                    "listening": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                },
                {
                    "speaking": [
                        {
                            "informatica": False
                        },
                        {
                            "deportes": False
                        }
                    ]
                }
            ]
        }
        user_registered_json = json.dumps(user_registered)
        with open("./userLoged.json","w") as file:
                try:
                    json.dump(user_registered_json,file,indent=4)
                except:
                    print("Error al insertar datos")
            
    except Exception as e:
        print(f"Ha fallado {e}")
    finally:
        cur.close()
        conn.close()
        root.destroy()
        Dashboard()