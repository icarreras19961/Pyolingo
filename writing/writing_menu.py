import tkinter as tk
import customtkinter as ctk

def writing_menu(contenedor):
    frameJuegoWriting = ctk.CTkFrame(
        contenedor, 
        fg_color="#f7f7f7"
    )
    frameJuegoWriting.pack_propagate(False)
    frameJuegoWriting.pack(fill="both", expand=True)

    lbTitulo = ctk.CTkLabel(
        frameJuegoWriting,
        text="Writing",
        text_color="#000"
    )
    lbTitulo.pack()