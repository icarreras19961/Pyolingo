import tkinter as tk
import customtkinter as ctk

btnVolerVentanas = []

def reading_menu(contenedor):
    frameReading = ctk.CTkFrame(
        contenedor, 
        fg_color="#f7f7f7"
    )
    frameReading.pack_propagate(False)
    frameReading.pack(fill="both", expand=True, pady=15)

    lbTitulo = ctk.CTkLabel(
        frameReading,
        text="Reading", 
        text_color="#000", 
        fg_color="transparent",
        font=("Arial", 36),
        anchor="w"
    )
    lbTitulo.pack(fill="x", pady=(0, 12), padx=30)

    linea = ctk.CTkLabel(
        frameReading,
        font=("Arial", 2),
        height=2,
        fg_color="#000"

    )
    linea.pack(fill="x", padx=30)

    frameContenidoReading = ctk.CTkFrame(
        frameReading,
        fg_color="transparent"
    )
    frameContenidoReading.pack_propagate(False)
    frameContenidoReading.pack(fill="both", expand=True)
    lbTitulo.pack()

    MenuCategorias(frameContenidoReading)


def MenuCategorias(contenedor):
    frameMenuCategorias = ctk.CTkFrame(
        contenedor,
        fg_color="#f7f7f7",
        
    )
    frameMenuCategorias.grid_columnconfigure(0, weight=1)
    frameMenuCategorias.grid_columnconfigure(1, weight=1)
    frameMenuCategorias.grid_columnconfigure(2, weight=1)
    frameMenuCategorias.grid_rowconfigure(0, weight=1)
    frameMenuCategorias.grid_rowconfigure(1, weight=1)
    frameMenuCategorias.pack(fill="both", expand=True)

    imgCategoriaTech = tk.PhotoImage(file="tech.png")
    btnCategoriaTech = ctk.CTkButton(
        frameMenuCategorias,
        text="TECH",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaTech,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top",
        command=lambda: JuegoReading(contenedor)
    )
    btnCategoriaTech.grid(row=0, column=0)

    imgCategoriaSports = tk.PhotoImage(file="sports.png")
    btnCategoriaSports = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaSports.grid(row=0, column=1)

    btnCategoriaPrueba1 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba1.grid(row=0, column=2)

    btnCategoriaPrueba2 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba2.grid(row=1, column=0)

    btnCategoriaPrueba3 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba3.grid(row=1, column=1)

    btnCategoriaPrueba4 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba4.grid(row=1, column=2)


btnColorDefault = "#EBEBEB"
btnColorDefaultHover = "#D9D9D9"

btnColorIncorrecto = "#CC3838"
btnColorIncorrectoHover = "#A52C2C"

btnColorCorrecto = "#48D46D"
btnColorCorrectoHover = "#3AAE59"


# CARGAR DATOS DEL JSON AQUI
def JuegoReading(contenedor):
    cerrarJuego(contenedor)

    frameJuego = ctk.CTkFrame(
        contenedor,
        fg_color="#f7f7f7",
    )
    frameJuego.pack_propagate(False)
    frameJuego.pack(fill="both", expand=True, pady=(12,0), padx=30)

    frameGrid = ctk.CTkFrame(
        frameJuego,
        fg_color="#f73"
    )
    frameGrid.grid_columnconfigure(0, weight=1)
    frameGrid.grid_columnconfigure(1, weight=1)
    frameGrid.grid_rowconfigure(0, weight=1)
    frameGrid.grid_rowconfigure(1, weight=1)
    frameGrid.pack(fill="both", expand=True)

    # 
    frameCard1 = ctk.CTkFrame(
        frameGrid,
        fg_color="#EBEBEB" 
    )
    frameCard1.pack_propagate(False)
    
    frameCard1.grid(row=0, column=1, sticky="nsew")

    lbCard1 = ctk.CTkLabel(
        frameCard1, 
        text="An office chair is designed for comfort and support during long working hours. It often includes adjustable height and wheels for mobility.",
        text_color="#000",
        font=("Arial", 18),
        anchor="w",
        justify="left",
        fg_color="transparent"
    )
    lbCard1.pack(fill="x", anchor="n")

    lbCard2 = ctk.CTkLabel(
        frameCard1, 
        text="An office chair is designed for comfort and support during long working hours. It often includes adjustable height and wheels for mobility.",
        text_color="#000",
        font=("Arial", 18),
        anchor="w",
        justify="left",
        fg_color="transparent"
    )
    lbCard2.pack(fill="x", anchor="s")

    # 
    frameCard2 = ctk.CTkFrame(
        frameGrid,
        fg_color="#D9D9D9" 
    )
    frameCard2.grid(row=0, column=0, sticky="nsew")

    frameCard3 = ctk.CTkFrame(
        frameGrid,
        fg_color="#CC3838" 
    )
    frameCard3.grid(row=1, column=0, sticky="nsew")

    frameCard4 = ctk.CTkFrame(
        frameGrid,
        fg_color="#48D46D" 
    )
    frameCard4.grid(row=1, column=1, sticky="nsew")

    # lbTextoJuegoReading = ctk.CTkLabel(
    #     frameGrid,
    #     text="An office chair is designed for comfort and support during long working hours. It often includes adjustable height and wheels for mobility.",
    #     text_color="#000",
    #     font=("Arial", 18),
    #     anchor="w",
    #     justify="left",
    #     fg_color="transparent"
    # )
    # # lbTextoJuegoReading.pack(fill="x", anchor="w")
    # lbTextoJuegoReading.grid(row = 0, column = 0)

    # ----------------------------------

    # lbPregunta = ctk.CTkLabel(
    #     frameJuego,
    #     text="¿Pregunta a responder?",
    #     text_color="#000",
    #     font=("Arial", 26),
    #     anchor="w",
    #     fg_color="transparent"         
    # )
    # lbPregunta.pack(anchor="w", pady=24)

    # btnRespuesta1 = ctk.CTkButton(
    #     frameJuego,
    #     text="A) Respuesta 1",
    #     text_color="#000",
    #     font=("Arial", 18),
    #     fg_color=btnColorDefault,
    #     hover_color=btnColorDefaultHover,
    #     anchor="w",
    #     width=300,
    #     height=50
    # )
    # btnRespuesta1.pack(anchor="w", pady=(0, 15))

    # btnRespuesta2 = ctk.CTkButton(
    #     frameJuego,
    #     text="B) Respuesta 2",
    #     text_color="#000",
    #     font=("Arial", 18),
    #     fg_color=btnColorCorrecto,
    #     hover_color=btnColorCorrectoHover,
    #     state="normal",
    #     anchor="w",
    #     width=300,
    #     height=50
    # )
    # btnRespuesta2.pack(anchor="w", pady=(0, 15))

    # btnRespuesta3 = ctk.CTkButton(
    #     frameJuego,
    #     text="C) Respuesta 3",
    #     text_color="#000",
    #     font=("Arial", 18),
    #     fg_color=btnColorIncorrecto,
    #     hover_color=btnColorIncorrectoHover,
    #     anchor="w",
    #     width=300,
    #     height=50
    # )
    # btnRespuesta3.pack(anchor="w", pady=(0, 15))

    # btnRespuesta4 = ctk.CTkButton(
    #     frameJuego,
    #     text="D) Respuesta 4",
    #     text_color="#000",
    #     font=("Arial", 18),
    #     fg_color=btnColorDefault,
    #     state="disabled",
    #     anchor="w",
    #     width=300,
    #     height=50
    # )
    # btnRespuesta4.pack(anchor="w", pady=(0, 15))



def cerrarJuego(juego):
    for child in juego.winfo_children():
        child.destroy()
