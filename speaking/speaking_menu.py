import tkinter as tk
import customtkinter as ctk

def speaking_menu(contenedor):
    frameJuegoSpeaking = ctk.CTkFrame(
        contenedor, 
        fg_color="#f7f7f7"
    )
    frameJuegoSpeaking.pack_propagate(False)
    frameJuegoSpeaking.pack(fill="both", expand=True)

    lbTitulo = ctk.CTkLabel(
        frameJuegoSpeaking,
        text="Speaking",
        text_color="#000"
    )
    lbTitulo.pack()