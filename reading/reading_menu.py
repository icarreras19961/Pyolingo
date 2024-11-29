import tkinter as tk
import customtkinter as ctk

def reading_menu(contenedor):
    frameJuegoReading = ctk.CTkFrame(
        contenedor, 
        fg_color="#f7f7f7"
    )
    frameJuegoReading.pack_propagate(False)
    frameJuegoReading.pack(fill="both", expand=True)

    lbTitulo = ctk.CTkLabel(
        frameJuegoReading,
        text="Reading",
        text_color="#000"
    )
    lbTitulo.pack()