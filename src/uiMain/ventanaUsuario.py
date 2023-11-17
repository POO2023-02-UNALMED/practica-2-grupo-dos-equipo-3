import tkinter as tk

class FieldFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.label = tk.Label(self, text="¡Hola desde FieldFrame!")
        self.label.pack()

        self.button = tk.Button(self, text="Haz clic", command=self.button_clicked)
        self.button.pack()

    def button_clicked(self):
        print("¡Botón clickeado!")


root = tk.Tk()

field_frame = FieldFrame(master=root)

# Iniciar el bucle de eventos de Tkinter
field_frame.mainloop()