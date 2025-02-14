import tkinter as tk
import customtkinter as ctk
from listening.listening_menu import listening_menu
from reading.reading_menu import reading_menu
from speaking.speaking_menu import speaking_menu
from writing.writing_menu import writing_menu
import forms.Login
import json

import json
import mariadb
import sys

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
    lbAvatar.pack(pady=(150, 20))
    with open("./userLoged.json","r") as file:
            data = json.load(file)
    json_object = json.loads(data)
    nombre = json_object["name"]
    
    lbNombreUsuario = ctk.CTkLabel(
        frameMenu, 
        text=nombre, 
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
    color = "#fff"
    btnInicio = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Inicio", 
        height=50,
        font=("Arial", 18, "bold"), 
        fg_color="#2F2F2F", 
        text_color=color, 
        hover_color="#454545",
        cursor="hand2",
        command=lambda: Inicio(frameContenedorJuegos)
    )
    btnInicio.pack(fill= "x", side="top", pady=(0,5))

    # ------------------------------
    btnPuntuaciones = ctk.CTkButton(
        frameContenedorOpcionesMenu, 
        text="Score", 
        height=50,
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
        height=50, 
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
        height=50, 
        font=("Arial", 16, "bold"), 
        fg_color="#2F2F2F", 
        text_color="#fff", 
        hover_color="#1B1E25", 
        cursor="hand2",
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
    btnWriting = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Writing",
        text_color="#000",
        font=("Arial", 40),
        image=imgWriting,
        fg_color="#f7f7f7",
        hover_color="#EBEBEB",
        compound="top",
        command=lambda: MostrarJuegoWriting(contenedor)
    )
    btnWriting.grid(row=0, column=0)

    imgReading = tk.PhotoImage(file="reading.png")
    btnReading = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Reading",
        text_color="#000",
        font=("Arial", 40),
        image=imgReading,
        fg_color="#f7f7f7",
        hover_color="#EBEBEB",
        compound="top",
        command=lambda: MostrarJuegoReading(contenedor)

    )
    btnReading.grid(row=0, column=1)

    imgListening = tk.PhotoImage(file="listening.png")
    btnListening = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Listening",
        text_color="#000",
        font=("Arial", 40),
        image=imgListening,
        fg_color="#f7f7f7",
        hover_color="#EBEBEB",
        compound="top",
        command=lambda: MostrarJuegoListening(contenedor)
    )
    btnListening.grid(row=1, column=0)

    imgSpeaking = tk.PhotoImage(file="speaking.png")
    btnSpeaking = ctk.CTkButton(
        frameContenedorMenuJuegos,
        text="Speaking",
        text_color="#000",
        font=("Arial", 40),
        image=imgSpeaking,
        fg_color="#f7f7f7",
        hover_color="#EBEBEB",
        compound="top",
        command=lambda: MostrarJuegoSpeaking(contenedor)
    )
    btnSpeaking.grid(row=1, column=1)

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
    # Aqui antes de cerrarlo todo voy ha tener que hace una actualizacion de la base de datos de nuestro usuario para que se guarde el progreso
    print("Inicia Login y se borra los datos del usuario guardados en userLoged.json")

    try:
        conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="pyolingo"
        )
    except mariadb.Error as e:
        print("Error de conexion a MariaDB: {e}")
        sys.exit(1)
    cur = conn.cursor()
    
    try:
        with open("./userLoged.json","r") as file:
            data = json.load(file)
        json_data = json.loads(data)
        
        nombreUser = json_data["name"]
        newlvl = json_data["lvl"]
        print(nombreUser)
        query = f"UPDATE usuario SET lvlComplete = '{json.dumps(newlvl)}'  WHERE nombre = '{nombreUser}'"
        
        cur.execute(query)
        conn.commit()
    except Exception as e:
        print(f"Fallo en la actualizacion del usuario: {e}")
    
    root.destroy()
    forms.Login.Login()