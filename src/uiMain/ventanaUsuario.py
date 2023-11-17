import tkinter as tk

class ventanaUsuario:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("UNTaller")
        self.ventana1.geometry("500x280")
        
        frame = tk.Frame(self.ventana1)
        frame.pack(expand=True, fill=tk.BOTH)

        menubar1 = tk.Menu(frame)
        self.ventana1.config(menu = menubar1)
        
        opciones1 = tk.Menu(menubar1,tearoff=0)
        menubar1.add_cascade(label="Archivo", menu=opciones1)    
        opciones1.add_command(label="Aplicación", command=self.fijarrojo)
        opciones1.add_command(label="Salir", command=self.ventana1.destroy)  
        
        opciones2 = tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="Procesos y Consultas", menu=opciones2) 
        opciones2.add_command(label="Funcionalidad 1")
        opciones2.add_command(label="Funcionalidad 2")
        opciones2.add_command(label="Funcionalidad 3")
        opciones2.add_command(label="Funcionalidad 4")
        opciones2.add_command(label="Funcionalidad 5")
               
        opciones3 = tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="Ayuda", menu=opciones3)  
        opciones3.add_command(label="Acerca de:", command=self.acercaDe)
        
              
        
        self.ventana1.mainloop()


    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def acercaDe(self):        
        ventanaSalida = tk.Tk()
        ventanaSalida.title("UNTallerAutores")
        ventanaSalida.geometry("470x170")
        textoSalida = "Programa realizado por:\n Manuela Chaverra\n Angelika Moya\n Jeronimo Gonzales\n Juan Sinitave\n En memoria de nuestros compitas que cancelaron"
        etiqueta = tk.Label(ventanaSalida, text=textoSalida, borderwidth=2, relief="solid", wraplength=770, font=16)
        etiqueta.grid(row=0, column=0, padx=10, pady=10)

if __name__ == "__main__":
    ventanaUsuario()