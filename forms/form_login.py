from tkinter import *
import customtkinter

def FormLogin():
        # Ventana principal
        root = customtkinter.CTk()
        root.title("Pyolingo")
        root.geometry("1200x650")
        root.resizable(False, False)

        # FrameMain 
        frameMain = Frame(root, bg="#f7f7f7")
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

        btnValidarUsuario = customtkinter.CTkButton(formularioLogin, text="Iniciar Sesión", font=("Arial", 20), width=170, height=50, anchor="center",text_color="black", fg_color=("black", "#FFCC00"), hover_color="#ECBD00", corner_radius=10)
        btnValidarUsuario.pack()
        
        root.mainloop()

FormLogin()