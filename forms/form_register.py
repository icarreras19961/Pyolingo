from tkinter import *
import customtkinter

def FormRegister(frameMain):

    formularioRegister = Frame(frameMain, width=400, height=500, bg="#f7f7f7")
    formularioRegister.pack_propagate(False)
    formularioRegister.pack(expand=True)

    # Contenido formulario Register
    lblRegisterTitulo = Label(formularioRegister, text="Register", font=("Arial", 32), bg="#f7f7f7")
    lblRegisterTitulo.pack(fill="x")

