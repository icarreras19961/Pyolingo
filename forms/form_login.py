from tkinter import *
import customtkinter
# Conexion imports
import mariadb
import sys

# Variables Globales
nombreLogin=""
pwdLogin=""


def FormLogin():
    # Ventana principal
    main = customtkinter.CTk()
    main.title("Pyolingo")
    main.geometry("1200x650")
    main.resizable(False, False)

    # Hacer una función para que te permita leer una imagen 
    # try:
    #     img = Image.open("../ref/img/logo.png")
    #     self.img = ImageTk.PhotoImage(img)
    # except Exception as e:
    #     print(f"Error loading image: {e}")
    #     self.img = None

    # FrameMain 
    frameMain = Frame(main, bg="#f7f7f7")
    frameMain.pack(fill="both", expand=True)
    frameMain.grid_columnconfigure(0, weight=1)
    frameMain.grid_columnconfigure(1, weight=1)
    frameMain.grid_rowconfigure(0, weight=1)

    # Contenedor donde estara el logo
    frameLogo = Frame(frameMain, bg="#FFCC00")
    frameLogo.grid(row=0, column=0, sticky="nsew")

    # Contenedor donde estara el formulario login
    frameLogin = Frame(frameMain, bg="#f7f7f7")
    frameLogin.grid(row=0, column=1, sticky="nsew")

    # Contenido FrameLogo
    img = PhotoImage(file="logo.png")
    lblLogoImg = Label(frameLogo, image=img, width=400, height=500, bg="#FFCC00")
    lblLogoImg.pack_propagate(False)
    lblLogoImg.pack(expand=True)

    lblLogo = customtkinter.CTkLabel(frameLogo, corner_radius=10, text="¿No tienes una cuenta?", bg_color="white", text_color="black", width=500, height=60, font=("Arial", 24), anchor="w")
    lblLogo.place(x=50, y=30)

    # Contenido FrameLogin
    formularioLogin = Frame(frameLogin, width=400, height=500, bg="#f7f7f7")
    formularioLogin.pack_propagate(False)
    formularioLogin.pack(expand=True)

    lblLoginTitulo = Label(formularioLogin, text="Login", font=("Arial", 32), bg="#f7f7f7")
    lblLoginTitulo.pack(fill="x")

    div1 = Frame(formularioLogin, bg="#f7f7f7", pady=40)
    div1.pack(fill="x")

    div2 = Frame(div1, bg="#f7f7f7", pady=11)
    div2.pack(fill="x")
    lblLoginNombre = Label(div2, text="Nombre de Usuario", font=("Arial", 16), anchor="w", pady=6, bg="#f7f7f7")
    lblLoginNombre.pack(fill="x")
    entryLoginNombre = customtkinter.CTkEntry(div2, placeholder_text="Ingresa tu usuario",font=("Arial", 14), height=50, text_color="black", fg_color=("black", "#EBEBEB"), corner_radius=10, border_color="#f7f7f7")
    entryLoginNombre.pack(fill="x")

    div3 = Frame(div1, bg="#f7f7f7", pady=11)
    div3.pack(fill="x")
    lblLoginPwd = Label(div3, text="Contraseña", font=("Arial", 16), anchor="w", pady=6, bg="#f7f7f7")
    lblLoginPwd.pack(fill="x")
    entryLoginPwd = customtkinter.CTkEntry(div3, placeholder_text="Ingresa tu contraseña", font=("Arial", 14), height=50, text_color="black", fg_color=("black", "#EBEBEB"), corner_radius=10, border_color="#f7f7f7")
    entryLoginPwd.pack(fill="x")

    btnValidarUsuario = customtkinter.CTkButton(formularioLogin, text="Iniciar Sesión", font=("Arial", 20), width=150, height=50, anchor="center",text_color="black", fg_color=("black", "#FFCC00"), hover_color="#ECBD00", corner_radius=10,command=conexionLogin)
    btnValidarUsuario.pack()
    
    main.mainloop()


def conexionLogin():
    try:
        conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="pyolingo"
        )
    except mariadb.Error as e:
        print("Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
        

    # Get Cursor
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM usuario "
    )

    for (reader) in cur:
        print(f"First Name: {reader[1]}, pwd: {reader[2]}")



FormLogin()