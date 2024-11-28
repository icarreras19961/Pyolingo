import tkinter as tk
import customtkinter as ctk
from listening.listening_menu import listening_menu
from reading.reading_menu import reading_menu
from speaking.speaking_menu import speaking_menu
from writing.writing_menu import writing_menu
import forms.Login

# 13151A
# FFCC00 Amarillo
# 2F2F2F Gris
def Dashboard():
    # Ventana principal
    root = ctk.CTk()
    root.title("Pyolingo")
    root.geometry("1200x750")
    root.minsize(1200, 750)
    root.grid_propagate(0)
    
    # FrameMain
    frameMain = ctk.CTkFrame(root, fg_color="#f7f7f7")
    frameMain.pack(fill="both", expand=True)
    frameMain.grid_columnconfigure(0, minsize=270)
    frameMain.grid_columnconfigure(1, weight=1)
    frameMain.grid_rowconfigure(0, weight=1)

    # Contenedor del Menú
    frameMenu = ctk.CTkFrame(
        frameMain, 
        fg_color="#FFCC00", 
        width=270,
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
    # lbNombreAplicacion = ctk.CTkLabel(
    #     frameMenu,
    #     text="Pyolingo", 
    #     text_color="#000", 
    #     font=("Arial", 32, "bold")
    # )
    # lbNombreAplicacion.pack(fill= "x", side="top", pady=20)

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
        font=("Arial", 24, "bold"), 
        fg_color="#FFCC00"
    )
    lbNombreUsuario.pack(pady=(0, 10))

    # --------------------- Contenedor de botones ------------------
    frameContenedorOpcionesMenu = ctk.CTkFrame(
        frameMenu, 
        fg_color="#FFCC00", 
        width=230,
        height=400
    )
    frameContenedorOpcionesMenu.pack_propagate(False)
    frameContenedorOpcionesMenu.pack(fill="y", expand=True)


    # Crear el fondo como un Frame o un Label
    btnInicio = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Inicio", 
        compound="left",
        height=50,
        font=("Arial", 18, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#454545",
        anchor="w",
        cursor="hand2",
        command=lambda: Inicio(frameContenedorJuegos)
    )
    btnInicio.pack(fill= "x", side="top", pady=(0,5))

    # ------------------------------
    # btnListening = ctk.CTkButton(
    #     frameContenedorOpcionesMenu, 
    #     text="Listening", 
    #     height=50, 
    #     font=("Arial", 16, "bold"), 
    #     fg_color="#13151A", 
    #     text_color="#fff", 
    #     hover_color="#1B1E25", 
    #     cursor="hand2",
    #     anchor="w",
    #     command=lambda: MostrarJuegoListening(frameContenedorJuegos)
    # )
    # btnListening.pack(fill= "x", side="top", pady=(0,5))

    # btnReading = ctk.CTkButton(
    #     frameContenedorOpcionesMenu, 
    #     text="Reading", 
    #     height=50, 
    #     font=("Arial", 16, "bold"), 
    #     fg_color="#13151A", 
    #     text_color="#fff", 
    #     hover_color="#1B1E25", 
    #     cursor="hand2",
    #     anchor="w",
    #     command=lambda: MostrarJuegoReading(frameContenedorJuegos)
    # )
    # btnReading.pack(fill= "x", side="top", pady=(0,5))

    # btnSpeaking = ctk.CTkButton(
    #     frameContenedorOpcionesMenu, 
    #     text="Speaking", 
    #     height=50,
    #     font=("Arial", 16, "bold"), 
    #     fg_color="#13151A", 
    #     text_color="#fff", 
    #     hover_color="#1B1E25", 
    #     cursor="hand2",
    #     anchor="w",
    #     command=lambda: MostrarJuegoSpeaking(frameContenedorJuegos)
    # )
    # btnSpeaking.pack(fill= "x", side="top", pady=(0,5))

    # btnWriting = ctk.CTkButton(
    #     frameContenedorOpcionesMenu, 
    #     text="Writing", 
    #     height=50,
    #     font=("Arial", 16, "bold"), 
    #     fg_color="#13151A", 
    #     text_color="#fff", 
    #     hover_color="#1B1E25", 
    #     cursor="hand2",
    #     anchor="w",
    #     command=lambda: MostrarJuegoWriting(frameContenedorJuegos)
    # )
    # btnWriting.pack(fill= "x", side="top", pady=(0,5))

    # ------------------------------
    btnPuntuaciones = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Score", 
        height=50,
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        anchor="w"
    )
    btnPuntuaciones.pack(fill= "x", side="top", pady=(0,5))

    btnAjustes = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Ajustes", 
        height=50, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        anchor="w"
    )
    btnAjustes.pack(fill= "x", side="top", pady=(0,5))

    btnCerrarSesion = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Cerrar Sesión", 
        height=50, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        anchor="w",
        command=lambda: cerrarSesion(root)
    )
    btnCerrarSesion.pack(fill= "x", side="top", pady=(0,5))
    Inicio(frameContenedorJuegos)
    root.mainloop()

def cerrarJuego(juego):
    for child in juego.winfo_children():
        child.destroy()

def Inicio(contenedor):
    cerrarJuego(contenedor)
    frameContenedorInicio = ctk.CTkFrame(contenedor, fg_color="#f7f7f7", corner_radius=0)
    frameContenedorInicio.pack(fill="both", expand=True, pady=15, padx=30)

    lbTituloInicio = ctk.CTkLabel(
        frameContenedorInicio, 
        text="Pyolingo", 
        text_color="#000", 
        fg_color="transparent",
        font=("Arial", 36),
        anchor="w"
    )
    lbTituloInicio.pack(fill="x", pady=(0, 12))

    linea = ctk.CTkLabel(
        frameContenedorInicio,
        font=("Arial", 2),
        height=2,
        fg_color="#000"

    )
    linea.pack(fill="x")

    frameContenedorMenuJuegos = ctk.CTkFrame(frameContenedorInicio, fg_color="transparent")
    frameContenedorMenuJuegos.grid_columnconfigure(0, weight=1)
    frameContenedorMenuJuegos.grid_columnconfigure(1, weight=1)
    frameContenedorMenuJuegos.grid_rowconfigure(0, weight=1)
    frameContenedorMenuJuegos.grid_rowconfigure(1, weight=1)
    frameContenedorMenuJuegos.pack(fill="both", expand=True)

    imgWriting = tk.PhotoImage(file="writing.png")
    btnWritinga = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Writing",
        text_color="#000",
        font=("Arial", 40),
        image=imgWriting,
        fg_color="#f7f7f7",
        hover_color="#2F2F2F",
        compound="top"
    )
    btnWritinga.grid(row=0, column=0)

    imgReading = tk.PhotoImage(file="reading.png")
    btnReadinga = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Reading",
        text_color="#000",
        font=("Arial", 40),
        image=imgReading,
        fg_color="#f7f7f7",
        hover_color="#2F2F2F",
        compound="top"
    )
    btnReadinga.grid(row=0, column=1)

    imgListening = tk.PhotoImage(file="listening.png")
    btnListeninga = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Listening",
        text_color="#000",
        font=("Arial", 40),
        image=imgListening,
        fg_color="#f7f7f7",
        hover_color="#2F2F2F",
        compound="top"
    )
    btnListeninga.grid(row=1, column=0)

    imgSpeaking = tk.PhotoImage(file="speaking.png")
    btnSpeakingo = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Speaking",
        text_color="#000",
        font=("Arial", 40),
        image=imgSpeaking,
        fg_color="#f7f7f7",
        hover_color="#2F2F2F",
        compound="top"
    )
    btnSpeakingo.grid(row=1, column=1)

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

Dashboard()