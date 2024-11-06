# La documentacion oficial
# https://docs.python.org/3/library/tk.html
# https://docs.python.org/es/3/library/tkinter.html
from tkinter import * 
import customtkinter

# from tkinter.ttk import *
from tkinter import messagebox as MessageBox


# Las finciones para lanzar las otras paginas
from writing.writing_menu import writing_menu
from speaking.speaking_menu import speaking_menu
from reading.reading_menu import reading_menu
from listening.listening_menu import listening_menu

def Dashboard():
    main = customtkinter.CTk()
    main.title("Pyolingo")
    main.geometry("1200x650")

    frameMain = Frame(main, bg="black")
    frameMain.pack(fill="both", expand=True)
    frameMain.grid_columnconfigure(0, weight=1)
    frameMain.grid_columnconfigure(1, weight=1)
    frameMain.grid_rowconfigure(0, weight=1)

    # Frame Menu -> donde estara los botones 
    frameMenu = Frame(frameMain)
    main.mainloop()

    #Frame 

# def donothing():
#    filewin = Toplevel(root)
#    button = Button(filewin, text="Do nothing button")
#    button.pack()

# root = Tk()

# def menu():
#     # Menu bar 
#     menubar = Menu(root)
#     filemenu = Menu(menubar, tearoff=0)
#     filemenu.add_command(label="New", command=donothing)
#     filemenu.add_command(label="Open", command=donothing)
#     filemenu.add_command(label="Save", command=donothing)
#     filemenu.add_command(label="Save as...", command=donothing)
#     filemenu.add_command(label="Close", command=donothing)

#     filemenu.add_separator()
#     filemenu.add_command(label="Exit", command=root.quit)
#     menubar.add_cascade(label="File", menu=filemenu)
#     editmenu = Menu(menubar, tearoff=0)
#     editmenu.add_command(label="Undo", command=donothing)
#     editmenu.add_separator()
#     editmenu.add_command(label="Cut", command=donothing)
#     editmenu.add_command(label="Copy", command=donothing)
#     editmenu.add_command(label="Paste", command=donothing)
#     editmenu.add_command(label="Delete", command=donothing)
#     editmenu.add_command(label="Select All", command=donothing)

#     menubar.add_cascade(label="Edit", menu=editmenu)
#     helpmenu = Menu(menubar, tearoff=0)
#     helpmenu.add_command(label="Help Index", command=donothing)
#     helpmenu.add_command(label="About...", command=donothing)
#     menubar.add_cascade(label="Help", menu=helpmenu)
#     root.config(menu=menubar)

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
# root.geometry("900x500")

# Lo que construye la app
# menu()
# opciones()
# root.mainloop()
Dashboard()
