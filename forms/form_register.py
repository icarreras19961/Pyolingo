import customtkinter as ctk
from dashboard import Dashboard

def FormRegister(root, contenedorDeFormulario):
    global entryRegisterUsuario
    global entryLoginPwd
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

    entryLoginPwd = ctk.CTkEntry(
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
    entryLoginPwd.pack(side="top", fill="x", pady=(0,40))

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
    # INSERT en la base de datos y Guardar el usuario que se acaba de resistrar userLoged
    # Destruimos todo la aplicacion de Login y iniciamos Dashboard
    cur = conexion().cursor()
    try:
        cur.execute(
            "SELECT * FROM usuario"
        )
    except:
        print("Ha fallado")
    
    reader = cur.fetchone()
    if(reader is None):
        print("Nada")
    else:
        print("puto alvaro")
    
    # root.destroy()
    # Dashboard()
