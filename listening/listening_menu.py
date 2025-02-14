import tkinter as tk
import customtkinter as ctk


btnColorDefault = "#EBEBEB"
# btnColorDefaultHover = "#D9D9D9"

btnColorIncorrecto = "#CC3838"
btnColorIncorrectoHover = "#A52C2C"

btnColorCorrecto = "#48D46D"
btnColorCorrectoHover = "#3AAE59"


def listening_menu(contenedor):
    frameListening = ctk.CTkFrame(
        contenedor, 
        fg_color="#f7f7f7"
    )
    frameListening.pack_propagate(False)
    frameListening.pack(fill="both", expand=True)

    lbTitulo = ctk.CTkLabel(
        frameListening,
        text="Listening", 
        text_color="#000", 
        fg_color="transparent",
        font=("Arial", 36),
        anchor="w"
    )
    lbTitulo.pack(fill="x", pady=(0, 12), padx=30)

    linea = ctk.CTkLabel(
        frameListening,
        font=("Arial", 2),
        height=2,
        fg_color="#000"

    )
    linea.pack(fill="x", padx=30)

    frameContenidoListening = ctk.CTkFrame(
        frameListening,
        fg_color="transparent"
    )
    frameContenidoListening.pack_propagate(False)
    frameContenidoListening.pack(fill="both", expand=True)
    lbTitulo.pack()

    MenuCategorias(frameContenidoListening)

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
        command=lambda: JuegoListening(contenedor)
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



# CARGAR DATOS DEL JSON AQUI
def JuegoListening(contenedor):
    cerrarJuego(contenedor)

    frameJuego = ctk.CTkFrame(
        contenedor,
        fg_color="#f7f7f7",
    )
    frameJuego.pack_propagate(False)
    frameJuego.pack(fill="both", expand=True, pady=(12,0), padx=30)

    frameGrid = ctk.CTkFrame(
        frameJuego,
        fg_color="#f7f7f7"
    )
    frameGrid.grid_columnconfigure(0, weight=1)
    frameGrid.grid_columnconfigure(1, weight=1)
    frameGrid.grid_rowconfigure(0, weight=1)
    frameGrid.grid_rowconfigure(1, weight=1)
    frameGrid.pack(fill="both", expand=True)

    #  ------------------------------------------------------
    frameCard1 = ctk.CTkFrame(
        frameGrid,
        fg_color=btnColorDefault
    )
    frameCard1.pack_propagate(False)
    frameCard1.grid_columnconfigure(0, weight=1)
    # frameCard1.grid_columnconfigure(1, weight=1)
    frameCard1.grid_rowconfigure(0, weight=1)
    frameCard1.grid_rowconfigure(1, minsize=100)
    frameCard1.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)


    # Aqui va el texto del json

    label1_text = tk.StringVar()
    label1_text.set("Write The Word")
    lbCard1 = ctk.CTkLabel(
        frameCard1,
        textvariable=label1_text,
        text_color="#000",
        font=("Arial", 18),
        justify="left",
        fg_color="transparent",
        # wraplength=320
    )
    lbCard1._name = 2
    lbCard1.grid(row=0, column=0, sticky="nsew")

    print(lbCard1._name)

    btnEscucharAudio = ctk.CTkButton(
        frameCard1,
        height=50,
        width=50,
        text="Play",
        text_color="#000",
        fg_color="#FFCC00",
        hover_color="#ECBD00"
    )
    btnEscucharAudio.grid(row=0, column=0, sticky="nsew")




    card1GridRespuesta = ctk.CTkFrame(
        frameCard1,
        fg_color="transparent",
    )
    card1GridRespuesta.grid_columnconfigure(0, weight=1)
    card1GridRespuesta.grid_columnconfigure(1, minsize=30)
    card1GridRespuesta.grid_rowconfigure(0, weight=1)
    card1GridRespuesta.grid(row=1, column=0)

    entryCard1 = ctk.CTkEntry(
        card1GridRespuesta,
        placeholder_text="Respuesta",
        text_color="#000", 
        font=("Arial", 16), 
        fg_color="#f7f7f7",
        height=50,
        width=300
    )
    entryCard1.grid(row=1, column=0, padx=20)
    
    # Boton 1 
    btnCardEnviarRespuesta1 = ctk.CTkButton(
        card1GridRespuesta,
        height=50,
        width=50,
        text="R",
        text_color="#000",
        fg_color="#FFCC00",
        hover_color="#ECBD00"

    )
    btnCardEnviarRespuesta1.grid(row=1, column=1, padx=(0,20))





    # -------------------------------------------------------------------
    frameCard2 = ctk.CTkFrame(
        frameGrid,
        fg_color=btnColorDefault
    )
    frameCard2.pack_propagate(False)
    frameCard2.grid_columnconfigure(0, weight=1)
    frameCard2.grid_rowconfigure(0, weight=1)
    frameCard2.grid_rowconfigure(1, minsize=100)
    frameCard2.grid(row=0, column=1, sticky="nsew", padx=50, pady=50)

    # Aqui va el texto del json
    lbCard2 = ctk.CTkLabel(
        frameCard2, 
        text="An office chair is designed for comfort and support during long working hours. It often includes adjustable height and wheels for mobility.",
        text_color="#000",
        font=("Arial", 18),
        justify="left",
        fg_color="transparent",
        wraplength=320
    )
    lbCard2.grid(row=0, column=0, sticky="nsew")

    card2GridRespuesta = ctk.CTkFrame(
        frameCard2,
        fg_color="transparent",
    )
    card2GridRespuesta.grid_columnconfigure(0, weight=1)
    card2GridRespuesta.grid_columnconfigure(1, minsize=30)
    card2GridRespuesta.grid_rowconfigure(0, weight=1)
    card2GridRespuesta.grid(row=1, column=0)

    entryCard2 = ctk.CTkEntry(
        card2GridRespuesta,
        placeholder_text="Respuesta",
        text_color="#000", 
        font=("Arial", 16), 
        fg_color="#f7f7f7",
        height=50,
        width=300
    )
    entryCard2.grid(row=0, column=0, padx=20)
    
    # Boton 2
    btnCard2 = ctk.CTkButton(
        card2GridRespuesta,
        height=50,
        width=50,
        text="R",
        text_color="#000",
        fg_color="#FFCC00",
        hover_color="#ECBD00"

    )
    btnCard2.grid(row=0, column=1, padx=(0,20))




    # -----------------------------------------------
    frameCard3 = ctk.CTkFrame(
        frameGrid,
        fg_color=btnColorDefault 
    )
    frameCard3.pack_propagate(False)
    frameCard3.grid_columnconfigure(0, weight=1)
    frameCard3.grid_rowconfigure(0, weight=1)
    frameCard3.grid_rowconfigure(1, minsize=100)
    frameCard3.grid(row=1, column=0, sticky="nsew", padx=50, pady=50)

    # Aqui va el texto del json
    lbCard3 = ctk.CTkLabel(
        frameCard3, 
        text="An office chair is designed for comfort and support during long working hours. It often includes adjustable height and wheels for mobility.",
        text_color="#000",
        font=("Arial", 18),
        justify="left",
        fg_color="transparent",
        wraplength=320
    )
    lbCard3.grid(row=0, column=0, sticky="nsew")

    card3GridRespuesta = ctk.CTkFrame(
        frameCard3,
        fg_color="transparent",
    )
    card3GridRespuesta.grid_columnconfigure(0, weight=1)
    card3GridRespuesta.grid_columnconfigure(1, minsize=30)
    card3GridRespuesta.grid_rowconfigure(0, weight=1)
    card3GridRespuesta.grid(row=1, column=0)

    entryCard3 = ctk.CTkEntry(
        card3GridRespuesta,
        placeholder_text="Respuesta",
        text_color="#000", 
        font=("Arial", 16), 
        fg_color="#f7f7f7",
        height=50,
        width=300
    )
    entryCard3.grid(row=0, column=0, padx=20)
    
    # Boton 3
    btnCard3 = ctk.CTkButton(
        card3GridRespuesta,
        height=50,
        width=50,
        text="R",
        text_color="#000",
        fg_color="#FFCC00",
        hover_color="#ECBD00"

    )
    btnCard3.grid(row=0, column=1, padx=(0,20))






    # -------------------------------------------------------------------------------
    frameCard4 = ctk.CTkFrame(
        frameGrid,
        fg_color=btnColorDefault 
    )
    frameCard4.pack_propagate(False)
    frameCard4.grid_columnconfigure(0, weight=1)
    frameCard4.grid_rowconfigure(0, weight=1)
    frameCard4.grid_rowconfigure(1, minsize=100)
    frameCard4.grid(row=1, column=1, sticky="nsew", padx=50, pady=50)

    # Aqui va el texto del json
    lbCard4 = ctk.CTkLabel(
        frameCard4, 
        text="An office chair is designed for comfort and support during long working hours. It often includes adjustable height and wheels for mobility.",
        text_color="#000",
        font=("Arial", 18),
        justify="left",
        fg_color="transparent",
        wraplength=320
    )
    lbCard4.grid(row=0, column=0, sticky="nsew")

    card4GridRespuesta = ctk.CTkFrame(
        frameCard4,
        fg_color="transparent",
    )
    card4GridRespuesta.grid_columnconfigure(0, weight=1)
    card4GridRespuesta.grid_columnconfigure(1, minsize=30)
    card4GridRespuesta.grid_rowconfigure(0, weight=1)
    card4GridRespuesta.grid(row=1, column=0)

    entryCard4 = ctk.CTkEntry(
        card4GridRespuesta,
        placeholder_text="Respuesta",
        text_color="#000", 
        font=("Arial", 16), 
        fg_color="#f7f7f7",
        height=50,
        width=300
    )
    entryCard4.grid(row=0, column=0, padx=20)
    
    # Boton 4
    btnCard4 = ctk.CTkButton(
        card4GridRespuesta,
        height=50,
        width=50,
        text="R",
        text_color="#000",
        fg_color="#FFCC00",
        hover_color="#ECBD00"

    )
    btnCard4.grid(row=0, column=1, padx=(0,20))
    
def cerrarJuego(juego):
    for child in juego.winfo_children():
        child.destroy()
