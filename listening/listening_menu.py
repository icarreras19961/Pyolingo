import tkinter as tk
import customtkinter as ctk

def listening_menu(contenedor):
    frameJuegoListening = ctk.CTkFrame(
        contenedor, 
        fg_color="#f7f7f7"
    )
    frameJuegoListening.pack_propagate(False)
    frameJuegoListening.pack(fill="both", expand=True)

    lbTitulo = ctk.CTkLabel(
        frameJuegoListening,
        text="Listening",
        text_color="#000"
    )
    lbTitulo.pack()
