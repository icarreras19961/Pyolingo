# La documentacion oficial
# https://docs.python.org/3/library/tk.html
# https://docs.python.org/es/3/library/tkinter.html

from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox as MessageBox


# Las finciones para lanzar las otras paginas
from writing.writing_menu import writing_menu
from speaking.speaking_menu import speaking_menu
from reading.reading_menu import reading_menu
from listening.listening_menu import listening_menu
from forms.form_login import FormLogin

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

root = Tk()

def opciones():
    boton1 = Button(root, text="Writing", command=writing_menu)
    boton1.grid(row=0, column=0)
   
    boton2 = Button(root, text="Speaking", command=speaking_menu)
    boton2.grid(row=1, column=0)

    boton3 = Button(root, text="Reading", command=reading_menu)
    boton3.grid(row=0, column=1)

    boton4 = Button(root, text="Listening", command=listening_menu)
    boton4.grid(row=1, column=1)

# El tamaño de la ventana
root.geometry("900x500")

# Lo que construye la app
# opciones()
# root.mainloop()
FormLogin()