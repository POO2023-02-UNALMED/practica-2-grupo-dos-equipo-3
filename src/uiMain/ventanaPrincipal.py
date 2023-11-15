from tkinter import *
import tkinter as tk

#global ventana 

def ventana_funcionalidades():
    ventana = Tk()
    ventana.title("UNTaller")
    ventana.geometry("500x300")

    frame = Frame(ventana, height=300, width=500)
    frame.pack()

    Label(frame, text="UNTaller", font=("Arial", 11)).grid(row=0, column=0)

    menuBar = tk.Menu(frame)

    # Crea opciones1 y opciones2 como submenús de menuBar
    opciones1 = tk.Menu(menuBar)
    opciones2 = tk.Menu(menuBar)

    # Añade opciones al submenú opciones1
    opciones1.add_command(label="Opción 1")
    opciones1.add_command(label="Opción 2")

    # Añade opciones al submenú opciones2
    opciones2.add_command(label="Opción 3")
    opciones2.add_command(label="Opción 4")

    # Añade los submenús al menú principal
    menuBar.add_cascade(label="Menu 1", menu=opciones1)
    menuBar.add_cascade(label="Menu 2", menu=opciones2)

    # Asigna el menú a la ventana
    ventana.config(menu=menuBar)

    ventana.mainloop()

def ventana_inicial():
    global ventana
    ventana = tk.Tk()
    ventana.title("Taller de Mecanica")
    ventana.geometry("1500x700")

    textoBreveDescripcion = "Bienvenido al sistema del Taller de Mecanica, en este espacio usted podrá administrar nóminas, inventarios, proveedores y repuestos dependiendo de su categoría de usuario. Garantizamos un acceso seguro y controlado a las diversas funciones y datos del programa"
    etiqueta = tk.Label(ventana, text=textoBreveDescripcion, borderwidth=2, relief="solid",  wraplength=770, font=16)
    etiqueta.grid(row=0, column=0, sticky='nw', padx=10, pady=10)

    menubar1 = tk.Menu(ventana)
    ventana.config(menu=menubar1)
    opciones1 = tk.Menu(menubar1)
    opciones1.add_command(label="salir", command = salirFunc)
    opciones1.add_command(label="descripcion", command = descripcionFunc)
    menubar1.add_cascade(label="Inicio", menu=opciones1)        
 
    bsumar = Button(text="ingresar",command=ingresarFunc).place(width=80, x=250,y=630)



    ventana.mainloop()


def salirFunc():
    global ventana
    ventana.withdraw()
    ventana1 = tk.Tk()
    ventana1.title("salir")
    ventana1.geometry("400x400")

    textoSalida = "Hasta pronto"
    etiqueta = tk.Label(ventana1, text=textoSalida, borderwidth=2, relief="solid",  wraplength=770, font=16)
    etiqueta.grid(row=0, column=0, padx=10, pady=10)

def descripcionFunc():
    global ventana
    textoDEscripcion = "Un Taller es una aplicación de escritorio diseñada para simplificar las tareas administrativas relacionadas con la reparación de automóviles en un taller mecánico. Esta aplicación abarca una amplia gama de aspectos cruciales para la gestión eficiente de un taller, incluyendo la administración de nóminas, inventarios, proveedores y repuestos. Lo que la distingue es su interfaz de usuario intuitiva y altamente personalizada que se adapta a las diferentes categorías de usuarios, garantizando un acceso seguro y controlado a las diversas funciones y datos del programa."
    etiqueta = tk.Label(ventana, text=textoDEscripcion, borderwidth=2, relief="solid",  wraplength=770, font=16)
    etiqueta.grid(row=2, column=0, sticky='n', padx=10, pady=10)

def ingresarFunc():
    global ventana
    ventana.withdraw()
    ventana_funcionalidades()

ventana_inicial()