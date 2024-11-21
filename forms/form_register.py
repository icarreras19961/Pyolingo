import customtkinter as ctk
from Dashboard import Dashboard
def FormRegister(root, contenedorDeFormulario):

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
    lbRegisterUsuario = ctk.CTkLabel(
        formularioRegister, 
        text="Email", 
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
    root.destroy()
    Dashboard()
