import tkinter as tk
import customtkinter as ctk

def reading_menu(contenedor):
    frameReading = ctk.CTkFrame(
        contenedor, 
        fg_color="#f7f7f7"
    )
    frameReading.pack_propagate(False)
    frameReading.pack(fill="both", expand=True, pady=15)

    lbTitulo = ctk.CTkLabel(
        frameReading,
        text="Reading", 
        text_color="#000", 
        fg_color="transparent",
        font=("Arial", 36),
        anchor="w"
    )
    lbTitulo.pack(fill="x", pady=(0, 12), padx=30)

    linea = ctk.CTkLabel(
        frameReading,
        font=("Arial", 2),
        height=2,
        fg_color="#000"

    )
    linea.pack(fill="x", padx=30)

    frameContenidoReading = ctk.CTkFrame(
        frameReading,
        fg_color="transparent"
    )
    frameContenidoReading.pack_propagate(False)
    frameContenidoReading.pack(fill="both", expand=True)
    lbTitulo.pack()

    MenuCategorias(frameContenidoReading)


def MenuCategorias(contenedor):
    frameMenuCategorias = ctk.CTkFrame(
        contenedor,
        fg_color="#f7f7f7",
        
    )
    frameMenuCategorias.grid_columnconfigure(0, weight=1)
    frameMenuCategorias.grid_columnconfigure(1, weight=1)
    frameMenuCategorias.grid_columnconfigure(2, weight=1)
    frameMenuCategorias.grid_rowconfigure(0, weight=1)
    frameMenuCategorias.grid_rowconfigure(1, weight=1)
    frameMenuCategorias.pack(fill="both", expand=True)

    imgCategoriaTech = tk.PhotoImage(file="tech.png")
    btnCategoriaTech = ctk.CTkButton(
        frameMenuCategorias,
        text="TECH",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaTech,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top",
        command=lambda: JuegoReading(contenedor)
    )
    btnCategoriaTech.grid(row=0, column=0)

    imgCategoriaSports = tk.PhotoImage(file="sports.png")
    btnCategoriaSports = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaSports.grid(row=0, column=1)

    btnCategoriaPrueba1 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba1.grid(row=0, column=2)

    btnCategoriaPrueba2 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba2.grid(row=1, column=0)

    btnCategoriaPrueba3 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba3.grid(row=1, column=1)

    btnCategoriaPrueba4 = ctk.CTkButton(
        frameMenuCategorias,
        text="SPORTS",
        font=("Arial", 30),
        text_color="#000",
        image=imgCategoriaSports,
        fg_color="#D9D9D9",
        hover_color="#EBEBEB",
        width=270,
        height=270,
        compound="top"
    )
    btnCategoriaPrueba4.grid(row=1, column=2)


def JuegoReading(contenedor):
    cerrarJuego(contenedor)

    frameJuego = ctk.CTkFrame(
        contenedor,
        fg_color="#f7f7f7",
    )
    frameJuego.pack_propagate(False)
    frameJuego.pack(fill="both", expand=True, pady=(12,0), padx=30)

    lbTextoJuegoReading = ctk.CTkLabel(
        frameJuego,
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce laoreet  nisi varius nisl porttitor, et scelerisque libero rutrum.Cras erat  lorem, eleifend rutrum nulla vitae, hendrerit mattis leo.\nFusce at  condimentum lectus. Curabitur vel iaculis ligula, quis lacinia sem.  Fusce in rutrum est, quis imperdiet leo.\nCurabitur feugiat consequat  nunc non porttitor.\nCras erat tellus, viverra eu molestie id, laoreet at ipsum. Aliquam erat volutpat.\nLorem ipsum dolor sit amet, consectetur  adipiscing elit.\nVivamus porta lacus mauris, at molestie elit egestas  sollicitudin.\nCurabitur porta maximus blandit. Fusce pretium lacus sit  amet lorem ultrices rutrum. Curabitur porta lorem ut magna lacinia, vel  rhoncus diam molestie.",
        text_color="#000",
        font=("Arial", 18),
        anchor="w",
        justify="left",
        fg_color="transparent"
    )
    lbTextoJuegoReading.pack(fill="x", anchor="w")

    # ----------------------------------

    lbPregunta = ctk.CTkLabel(
        frameJuego,
        text="Pregunta",
        text_color="#000",
        font=("Arial", 24),
        anchor="w",
        fg_color="transparent"         
    )
    lbPregunta.pack(anchor="w", pady=24)

    


def cerrarJuego(juego):
    for child in juego.winfo_children():
        child.destroy()
