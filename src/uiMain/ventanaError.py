import tkinter as tk

class ventanaError(): 
    def __init__(self, texto):
        self.texto = texto
        self.ventanaSalida = tk.Tk()
        self.ventanaSalida.title("ERROR")
        self.ventanaSalida.geometry("400x300")
        self.etiqueta = tk.Label(self.ventanaSalida, text=self.texto, wraplength=770, font=8)
        self.etiqueta.grid(row=0, column=0, padx=10, pady=10)
        self.ventanaSalida.mainloop()

    