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
    frameMain.grid_columnconfigure(0, minsize=250)
    frameMain.grid_columnconfigure(1, weight=1)
    frameMain.grid_rowconfigure(0, weight=1)

    # Contenedor del Menú
    frameMenu = ctk.CTkFrame(
        frameMain, 
        fg_color="#222222", 
        width=250,
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
        bg="#13151A"
    )
    lbAvatar.image = img
    lbAvatar.pack(pady=(20, 20))

    lbNombreUsuario = ctk.CTkLabel(
        frameMenu, 
        text="Nombre Usuario", 
        text_color="#000",
        font=("Arial", 16, "bold"), 
        fg_color="#13151A"
    )
    lbNombreUsuario.pack(pady=(0, 10))

    # --------------------- Contenedor de botones ------------------
    frameContenedorOpcionesMenu = ctk.CTkFrame(
        frameMenu, 
        fg_color="#222222", 
        width=220,
        height=400
    )
    frameContenedorOpcionesMenu.pack_propagate(False)
    frameContenedorOpcionesMenu.pack(fill="y", expand=True)


    # Crear el fondo como un Frame o un Label
    iconInicio = tk.PhotoImage(file="home.png")
    btnInicio = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Inicio", 
        compound="left",
        height=50,
        font=("Arial", 18, "bold"), 
        fg_color="#222222", 
        text_color="#fff", 
        hover_color="#454545",
        anchor="w",
        cursor="hand2",
        command=lambda: Inicio(frameContenedorJuegos)
    )
    btnInicio.pack(fill= "x", side="top", pady=(0,5))

    # ------------------------------
    btnListening = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Listening", 
        height=50, 
        font=("Arial", 16, "bold"), 
        fg_color="#13151A", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        anchor="w",
        command=lambda: MostrarJuegoListening(frameContenedorJuegos)
    )
    btnListening.pack(fill= "x", side="top", pady=(0,5))

    btnReading = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Reading", 
        height=50, 
        font=("Arial", 16, "bold"), 
        fg_color="#13151A", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        anchor="w",
        command=lambda: MostrarJuegoReading(frameContenedorJuegos)
    )
    btnReading.pack(fill= "x", side="top", pady=(0,5))

    btnSpeaking = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Speaking", 
        height=50,
        font=("Arial", 16, "bold"), 
        fg_color="#13151A", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        anchor="w",
        command=lambda: MostrarJuegoSpeaking(frameContenedorJuegos)
    )
    btnSpeaking.pack(fill= "x", side="top", pady=(0,5))

    btnWriting = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Writing", 
        height=50,
        font=("Arial", 16, "bold"), 
        fg_color="#13151A", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
        anchor="w",
        command=lambda: MostrarJuegoWriting(frameContenedorJuegos)
    )
    btnWriting.pack(fill= "x", side="top", pady=(0,5))

    # ------------------------------
    btnPuntuaciones = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Score", 
        height=50,
        font=("Arial", 16, "bold"), 
        fg_color="#13151A", 
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
        fg_color="#13151A", 
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
        fg_color="#13151A", 
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

    frameContenedorWriting = ctk.CTkFrame(
        frameContenedorInicio,
        width=300,
        height=300,
        fg_color="red"
    )
    frameContenedorWriting.place(relx=0.2, rely=0.3, anchor="center")

    frameContenedorReading = ctk.CTkFrame(
        frameContenedorInicio,
        width=300,
        height=300,
        fg_color="red"
    )
    frameContenedorReading.place(relx=0.8, rely=0.3, anchor="center")

    # frameContenedorWriting = ctk.CTkFrame(
    #     frameContenedorInicio,
    #     width=300,
    #     height=300,
    #     fg_color="blue"
    # )
    # frameContenedorWriting.place(relx=0.3, rely=0.4, anchor="center")

    # frameContenedorWriting = ctk.CTkFrame(
    #     frameContenedorInicio,
    #     width=300,
    #     height=300,
    #     fg_color="blue"
    # )
    # frameContenedorWriting.place(relx=0.3, rely=0.4, anchor="center")


    # writingImage = tk.PhotoImage(file="writingImage.png")
    # btnMostrarWriting = ctk.CTkButton(
    #     frameContenedorInicio,
    #     text="Writing",
    #     text_color="#000",
    #     image=writingImage,
    #     fg_color="transparent",
    #     hover="#f7f7f7",
    #     cursor="hand2",
    #     font=("Arial", 32, "bold"),
    #     compound="top"

    # )
    # btnMostrarWriting.place(x=100, y=100)

    # frameInicioContenido = ctk.CTkFrame(contenedor, fg_color="red")
    # frameInicioContenido.columnconfigure(0, minsize=300)
    # frameInicioContenido.columnconfigure(1, minsize=300)
    # frameInicioContenido.rowconfigure(0, minsize=300)
    # frameInicioContenido.rowconfigure(1, minsize=300)
    # frameInicioContenido.pack(fill="both", expand=True)

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