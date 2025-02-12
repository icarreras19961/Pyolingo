import tkinter as tk
import customtkinter as ctk
from random import *
import json


btnVolerVentanas = []

btnColorDefault = "#EBEBEB"
# btnColorDefaultHover = "#D9D9D9"

btnColorIncorrecto = "#CC3838"
btnColorIncorrectoHover = "#A52C2C"

btnColorCorrecto = "#48D46D"
btnColorCorrectoHover = "#3AAE59"


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


# Cubos de texto

juego1 = None
juego2 = None
juego3 = None
juego4 = None

# CARGAR DATOS DEL JSON AQUI
def JuegoReading(contenedor):
    global juego1
    global juego2
    global juego3
    global juego4
    
    rellenador()
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
    frameCard1.grid_rowconfigure(0, weight=1)
    frameCard1.grid_rowconfigure(1, minsize=100)
    frameCard1.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

    # Aqui va el texto del json
    lbCard1 = ctk.CTkLabel(
        frameCard1, 
        text=juego1.descripcion,
        text_color="#000",
        font=("Arial", 18),
        justify="left",
        fg_color="transparent",
        wraplength=320
    )
    lbCard1.grid(row=0, column=0, sticky="nsew")

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
    entryCard1.grid(row=0, column=0, padx=20)
    
    # Boton 1 
    btnCard1 = ctk.CTkButton(
        card1GridRespuesta,
        height=50,
        width=50,
        text="R",
        text_color="#000",
        fg_color="#FFCC00",
        hover_color="#ECBD00",
        command=lambda: AnalizarRespuesta(1,entryCard1.get(),frameCard1)
        

    )
    btnCard1.grid(row=0, column=1, padx=(0,20))





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
        text=juego2.descripcion,
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
        hover_color="#ECBD00",
        command=lambda: AnalizarRespuesta(2,entryCard2.get(),frameCard2)
        

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
        text=juego3.descripcion,
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
        hover_color="#ECBD00",
        command=lambda: AnalizarRespuesta(3,entryCard3.get(),frameCard3)
        

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
        text=juego4.descripcion,
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
        hover_color="#ECBD00",
        command=lambda: AnalizarRespuesta(4,entryCard4.get(),frameCard4)

    )
    btnCard4.grid(row=0, column=1, padx=(0,20))

    
#Necesitamos rellenar los cuandraditos primero
def rellenador():
    # La array que decide que aparece
    nrand=[randomizador(),randomizador(),randomizador(),randomizador()]
    # Las globales
    global juego1
    global juego2
    global juego3
    global juego4
    
    # El fichero de donde sale la info
    with open("./reading/Informatica/informatica_reading.json","r") as file:
        data = json.load(file)
        
    # La asignacion de los objetos
    juego1 = Juego(data[nrand[0]]["descripcion"], data[nrand[0]]["respuesta"])
    juego2 = Juego(data[nrand[1]]["descripcion"], data[nrand[1]]["respuesta"])
    juego3 = Juego(data[nrand[2]]["descripcion"], data[nrand[2]]["respuesta"])
    juego4 = Juego(data[nrand[3]]["descripcion"], data[nrand[3]]["respuesta"])

def randomizador():
    return randrange(1,20)

correcto1 = False
correcto2 = False
correcto3 = False
correcto4 = False
# Empieza el metodo juego
def AnalizarRespuesta(*respuesta):
    global btnColorDefault
    global correcto1
    global correcto2
    global correcto3
    global correcto4
    # Falta que detecte cuando ha acabado el juego
    if(respuesta[0] == 4):
        resultado = juego4.respuesta.lower() == respuesta[1].lower()
        print(juego4.respuesta)
        if(resultado):
            respuesta[2].configure(fg_color="#48D46D")
            correcto4 = True         
        else:
            respuesta[2].configure(fg_color="#CC3838")
    elif (respuesta[0] == 3):
        resultado = juego3.respuesta.lower() == respuesta[1].lower()
        print(juego3.respuesta)
        if(resultado):
            respuesta[2].configure(fg_color="#48D46D")
            correcto3 = True 
        else:
            respuesta[2].configure(fg_color="#CC3838")
    elif (respuesta[0] == 2):
        resultado = juego2.respuesta.lower() == respuesta[1].lower()
        print(juego2.respuesta)
        if(resultado):
            respuesta[2].configure(fg_color="#48D46D")
            correcto2 = True
        else:
            respuesta[2].configure(fg_color="#CC3838")
    elif (respuesta[0] == 1):
        resultado = juego1.respuesta.lower() == respuesta[1].lower()
        print(juego1.respuesta)
        if(resultado):
            respuesta[2].configure(fg_color="#48D46D")
            correcto1 = True
        else:
            respuesta[2].configure(fg_color="#CC3838")
    
    # lo que va dentro del if de abajo = correcto1 and correcto2 and correcto3 and correcto4
    if (True):
        print("Has ganado")
        # Aqui tendremos
        with open("./userLoged.json","r") as file:
            data = json.load(file)
        print(data["reading"]["informatica"])


def cerrarJuego(juego):
    for child in juego.winfo_children():
        child.destroy()

# Clase para las preguntas respuestas
class Juego:
    def __init__(self, descripcion, respuesta):
        self.descripcion = descripcion
        self.respuesta = respuesta
    
    def getDesc(self):
        return self.descripcion
    
    # comparador de respuesta
    def comprobar_resp(self, resp_user):
        if(self.respuesta == resp_user):
            return True
        else:
            return False