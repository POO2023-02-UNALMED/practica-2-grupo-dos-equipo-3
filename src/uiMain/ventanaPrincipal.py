from tkinter import *
import tkinter as tk

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





