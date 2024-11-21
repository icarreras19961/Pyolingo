import tkinter as tk
import customtkinter as ctk
from .form_login import FormLogin
from .form_register import FormRegister

def on_enter(event, button, textColor):
    button.configure(text_color=textColor)  # Cambiar color de texto a rojo cuando el ratón entra

def on_leave(event, button, textColor):
    button.configure(text_color=textColor)


def MostrarFormularioLogin(root, frameContenedorFormulario, frameContenedorLogo):
    for child in frameContenedorFormulario.winfo_children():
        child.destroy()

    FormLogin(root, frameContenedorFormulario)

    lbMensajeLogoInicio = ctk.CTkLabel(
        frameContenedorLogo, 
        text="¿No tienes una cuenta?", 
        text_color="#000",font=("Arial", 24),
        fg_color="#f7f7f7", 
        width=500, 
        height=60, 
        anchor="w", 
        corner_radius=10
    )
    lbMensajeLogoInicio.place(relx=0.5, rely=0.1, anchor="center")

    btnRegistrarse = ctk.CTkButton(
        frameContenedorLogo, 
        width=0, 
        height=60, 
        text="Registrate", 
        fg_color="#f7f7f7",
        text_color="#FFCC00", 
        font=("Arial", 24, "bold"), 
        corner_radius=0, 
        cursor="hand2", 
        hover_color="#f7f7f7",
        command=lambda: MostrarFormularioRegister(root, frameContenedorFormulario, frameContenedorLogo)
    )
    btnRegistrarse.place(rely=0.1, x=380, anchor="center")

    lbMensajeRegistrarseFinal = ctk.CTkLabel(
        frameContenedorLogo, 
        text="ya.", 
        fg_color="#f7f7f7", 
        text_color="black",
        height=60, 
        font=("Arial", 24),
        anchor="w"
    )
    lbMensajeRegistrarseFinal.place(x=460, rely=0.1, anchor="center")

    btnRegistrarse.bind("<Enter>", lambda event, button=btnRegistrarse: on_enter(event, button, "#D1A800"))
    btnRegistrarse.bind("<Leave>", lambda event, button=btnRegistrarse: on_leave(event, button, "#FFCC00"))

def MostrarFormularioRegister(root, frameContenedorFormulario, frameContenedorLogo):
    for child in frameContenedorFormulario.winfo_children():
        child.destroy()

    FormRegister(root, frameContenedorFormulario)

    lbMensajeLogoInicio = ctk.CTkLabel(
        frameContenedorLogo, 
        text="¿Ya tienes una cuenta?", 
        text_color="#000",
        font=("Arial", 24),
        fg_color="#f7f7f7", 
        width=500, 
        height=60, 
        anchor="w", 
        corner_radius=10
    )
    lbMensajeLogoInicio.place(relx=0.5, rely=0.1, anchor="center")

    btnIniciarSesion = ctk.CTkButton(
        frameContenedorLogo, 
        width=0, 
        height=60, 
        text="Inicia Sesion", 
        fg_color="#f7f7f7", 
        text_color="#FFCC00", 
        font=("Arial", 24, "bold"), 
        corner_radius=0, 
        cursor="hand2", 
        hover_color="#f7f7f7",
        command=lambda: MostrarFormularioLogin(root, frameContenedorFormulario, frameContenedorLogo)
    )
    btnIniciarSesion.place(rely=0.1, x=395, anchor="center")

    btnIniciarSesion.bind("<Enter>", lambda event, button=btnIniciarSesion: on_enter(event, button, "#D1A800"))
    btnIniciarSesion.bind("<Leave>", lambda event, button=btnIniciarSesion: on_leave(event, button, "#FFCC00"))

def Login():
    root = ctk.CTk()
    root.title("Pyolingo")
    root.geometry("1200x650")
    root.resizable(False, False)

    frameContenedor = ctk.CTkFrame(root, fg_color="#fff")
    frameContenedor.grid_columnconfigure(0, minsize=600)
    frameContenedor.grid_columnconfigure(1, minsize=600)
    frameContenedor.grid_rowconfigure(0, weight=1)
    frameContenedor.pack(fill="both", expand=True)

    frameContenedorLogo = ctk.CTkFrame(
        frameContenedor, 
        fg_color="#FFCC00", 
        corner_radius=0, 
        width=600
    )
    frameContenedorLogo.grid(row=0, column=0, sticky="nsew")

    imgLogo = tk.PhotoImage(file="logo.png")
    lbLogo = tk.Label(
        frameContenedorLogo, 
        image=imgLogo, 
        bg="#FFCC00"
    )
    lbLogo.place(relx=0.5, rely=0.5, anchor="center")

    frameContenedorFormulario = ctk.CTkFrame(
        frameContenedor, 
        fg_color="#f7f7f7"
    )
    frameContenedorFormulario.grid(row=0, column=1, sticky="nsew")
    MostrarFormularioLogin(root, frameContenedorFormulario, frameContenedorLogo)
    root.mainloop()