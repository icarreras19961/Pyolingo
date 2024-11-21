import tkinter as tk
import customtkinter as ctk
from listening.listening_menu import listening_menu
from reading.reading_menu import reading_menu
from speaking.speaking_menu import speaking_menu
from writing.writing_menu import writing_menu
import forms.Login


# FFCC00 Amarillo
# 2F2F2F Gris
def Dashboard():
    # Ventana principal
    root = ctk.CTk()
    root.title("Pyolingo")
    root.geometry("1200x650")
    root.grid_propagate(0)
    
    # FrameMain
    frameMain = ctk.CTkFrame(root, fg_color="#f7f7f7")
    frameMain.pack(fill="both", expand=True)
    frameMain.grid_columnconfigure(0, minsize=300)
    frameMain.grid_columnconfigure(1, weight=1)
    frameMain.grid_rowconfigure(0, weight=1)

    # Contenedor del Menú
    frameMenu = ctk.CTkFrame(
        frameMain, 
        fg_color="#FFCC00", 
        width=300,
        corner_radius=0
    )
    frameMenu.grid(row=0, column=0, sticky="nsew")

    # Contenedor del Contenido
    frameContenedorJuegos = ctk.CTkFrame(
        frameMain, 
        fg_color="#f7f7f7"
    )
    frameContenedorJuegos.grid(row=0, column=1, sticky="nsew")
    frameContenedorJuegos.pack_propagate(False)

    # Nombre de la Aplicación
    lbNombreAplicacion = ctk.CTkLabel(
        frameMenu,
        text="Pyolingo", 
        text_color="#000", 
        font=("Arial", 32, "bold")
    )
    lbNombreAplicacion.pack(fill= "x", side="top", pady=20)

    # Contenido Menú 
    img = tk.PhotoImage(file="avatar.png")
    lbAvatar = tk.Label(
        frameMenu, 
        image=img, 
        bg="#FFCC00"
    )
    lbAvatar.image = img
    lbAvatar.pack(pady=(20, 20))

    lbNombreUsuario = ctk.CTkLabel(
        frameMenu, 
        text="Nombre Usuario", 
        text_color="#000",
        font=("Arial", 16, "bold"), 
        fg_color="#FFCC00"
    )
    lbNombreUsuario.pack(pady=(0, 10))

    # --------------------- Contenedor de botones ------------------
    frameContenedorOpcionesMenu = ctk.CTkFrame(
        frameMenu, 
        fg_color="#FFCC00", 
        width=250,
        height=400
    )
    frameContenedorOpcionesMenu.pack_propagate(False)
    frameContenedorOpcionesMenu.pack(fill="y", expand=True)

    btnInicio = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Inicio", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2"
    )
    btnInicio.pack(fill= "x", side="top", pady=(0,5))

    # ------------------------------
    btnListening = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Listening", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        command=lambda: MostrarJuegoListening(frameContenedorJuegos)
    )
    btnListening.pack(fill= "x", side="top", pady=(0,5))

    btnReading = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Reading", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        command=lambda: MostrarJuegoReading(frameContenedorJuegos)
    )
    btnReading.pack(fill= "x", side="top", pady=(0,5))

    btnSpeaking = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Speaking", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        command=lambda: MostrarJuegoSpeaking(frameContenedorJuegos)
    )
    btnSpeaking.pack(fill= "x", side="top", pady=(0,5))

    btnWriting = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Writing", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        command=lambda: MostrarJuegoWriting(frameContenedorJuegos)
    )
    btnWriting.pack(fill= "x", side="top", pady=(0,5))

    # ------------------------------
    btnPuntuaciones = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Score", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2"
    )
    btnPuntuaciones.pack(fill= "x", side="top", pady=(0,5))

    btnAjustes = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Ajustes", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2"
    )
    btnAjustes.pack(fill= "x", side="top", pady=(0,5))

    btnCerrarSesion = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Cerrar Sesión", 
        height=40, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        command=lambda: cerrarSesion(root)
    )
    btnCerrarSesion.pack(fill= "x", side="top", pady=(0,5))

    root.mainloop()

def cerrarJuego(juego):
    for child in juego.winfo_children():
        child.destroy()

def MostrarJuegoListening(contenedor):
    cerrarJuego(contenedor)
    listening_menu(contenedor)

def MostrarJuegoReading(contenedor):
    cerrarJuego(contenedor)
    reading_menu(contenedor)

def MostrarJuegoSpeaking(contenedor):
    cerrarJuego(contenedor)
    speaking_menu(contenedor)

def MostrarJuegoWriting(contenedor):
    cerrarJuego(contenedor)
    writing_menu(contenedor)

def cerrarSesion(root):
    root.destroy()
    forms.Login.Login()
    print("Inicia Login y se borra los datos del usuario guardados en userLoged.json")

def readFile():
    # leer el fichero json y guardarlo en variables para rellenar el dashboard
    print("hola")
