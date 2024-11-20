from tkinter import *
import customtkinter

# FFCC00 Amarillo
# 2F2F2F Gris
def Dashboard():
    # Ventana principal
    main = customtkinter.CTk()
    main.title("Pyolingo")
    main.geometry("1200x650")
    main.grid_propagate(0)
    
    # FrameMain
    frameMain = Frame(main, bg="#f7f7f7")
    frameMain.pack(fill="both", expand=True)
    frameMain.grid_columnconfigure(0, minsize=300)
    frameMain.grid_columnconfigure(1, weight=1)
    frameMain.grid_rowconfigure(0, weight=1)

    # Contenedor del Menú
    frameMenu = Frame(frameMain, bg="#FFCC00", width=300)
    frameMenu.grid(row=0, column=0, sticky="nsew")

    # Contenedor del Contenido
    frameContenido = Frame(frameMain, bg="#f7f7f7")
    frameContenido.grid(row=0, column=1, sticky="nsew")

    # Contenido Menú 
    img = PhotoImage(file="avatar.png")
    lblAvatar = Label(frameMenu, image=img, bg="#FFCC00")
    lblAvatar.image = img
    lblAvatar.pack(pady=(50, 20))

    lblNombreUsuario = Label(frameMenu, text="Nombre Usuario", font=("Arial", 16, "bold"), bg="#FFCC00")
    lblNombreUsuario.pack(pady=(0, 10))

    # Contenedor de botones 
    frameContenedorOpcionesMenu = Frame(frameMenu, bg="#FFCC00", width=250, height=400)
    frameContenedorOpcionesMenu.pack_propagate(False)
    frameContenedorOpcionesMenu.pack(fill="y", expand=True)

    btnPuntuaciones = customtkinter.CTkButton(frameContenedorOpcionesMenu, text="Score", height=40, font=("Arial", 16, "bold"), fg_color="#2F2F2F", text_color="#fff", hover_color="#1B1E25", cursor="hand2")
    btnPuntuaciones.pack(fill= "x", side="top", pady=(0,5))

    btnAjustes = customtkinter.CTkButton(frameContenedorOpcionesMenu, text="Ajustes", height=40, font=("Arial", 16, "bold"), fg_color="#2F2F2F", text_color="#fff", hover_color="#1B1E25", cursor="hand2")
    btnAjustes.pack(fill= "x", side="top", pady=(0,5))

    btnAjustes = customtkinter.CTkButton(frameContenedorOpcionesMenu, text="Salir", height=40, font=("Arial", 16, "bold"), fg_color="#2F2F2F", text_color="#fff", hover_color="#1B1E25", cursor="hand2")
    btnAjustes.pack(fill= "x", side="bottom", pady=(0,5))


    # Función para centrar la imagen
    def centrar_imagen_horizontal():
        frame_width = frameMenu.winfo_width()
        frame_height = frameMenu.winfo_height()
        img_width = img.width()
        # img_height = img.height()

        # Calcular posición para centrar
        x = (frame_width - img_width) // 2
        # y = (frame_height - img_height) // 2

        # Reposicionar la imagen
        lblAvatar.place(x=x, y=70)
        # lblNombreUsuario.place(x=x, y=230)

    # Llamar a centrar_imagen después de renderizar
    # frameMenu.after(100, centrar_imagen_horizontal)

    main.mainloop()

def readFile():
    # leer el fichero json y guardarlo en variables para rellenar el dashboard
    print("hola")

readFile()
Dashboard()