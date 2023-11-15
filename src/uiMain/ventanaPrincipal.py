import tkinter as tk

class MiAplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi Aplicación")
        self.ventana.geometry("800x600")

        # Zona 0: Título de la aplicación
        frame_titulo = tk.Frame(self.ventana, bg="red", height=50)
        tk.Label(frame_titulo, text="Título de la Aplicación", font=("Arial", 14), bg="red", fg="white").pack(fill=tk.BOTH, expand=True)
        frame_titulo.pack(fill=tk.X)

        # Zona 1: Menús y funcionalidades
        frame_menu = tk.Frame(self.ventana, bg="red", width=200)
        # Agrega tus menús y funcionalidades aquí
        # Por ejemplo:
        tk.Label(frame_menu, text="Menús y Funcionalidades", font=("Arial", 12), bg="red", fg="white").pack(pady=10)
        tk.Button(frame_menu, text="Opción 1", command=self.opcion1).pack(pady=5)
        tk.Button(frame_menu, text="Opción 2", command=self.opcion2).pack(pady=5)
        frame_menu.pack(side=tk.LEFT, fill=tk.Y)

        # Zona 2: Componentes de interfaz para manejar información
        frame_interfaz = tk.Frame(self.ventana, bg="blue", width=600)
        # Agrega tus componentes de interfaz aquí
        # Por ejemplo:
        tk.Label(frame_interfaz, text="Componentes de Interfaz", font=("Arial", 12), bg="blue", fg="white").pack(pady=10)
        tk.Entry(frame_interfaz).pack(pady=5)
        tk.Button(frame_interfaz, text="Realizar Consulta", command=self.realizar_consulta).pack(pady=5)
        frame_interfaz.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
    def opcion1(self):
        print("Opción 1 seleccionada")

    def opcion2(self):
        print("Opción 2 seleccionada")

    def realizar_consulta(self):
        print("Consulta realizada")

class VentanaInicial:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Mi Aplicación")
        self.ventana1.geometry("800x600")

        textoBreveDescripcion = "Bienvenido al sistema del Taller de Mecanica, en este espacio usted podrá administrar nóminas, inventarios, proveedores y repuestos dependiendo de su categoría de usuario. Garantizamos un acceso seguro y controlado a las diversas funciones y datos del programa"
        etiqueta = tk.Label(self.ventana1, text=textoBreveDescripcion, borderwidth=2, relief="solid", wraplength=770, font=16)
        etiqueta.grid(row=0, column=0, sticky='nw', padx=10, pady=10)

        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="salir", command=self.salirFunc)
        opciones1.add_command(label="descripcion", command=self.descripcionFunc)
        menubar1.add_cascade(label="Inicio", menu=opciones1)

        bsumar = tk.Button(self.ventana1, text="ingresar", command=self.ingresarFunc)
        bsumar.place(width=80, x=250, y=500)
        self.ventana1.mainloop()

    def salirFunc(self):
        self.ventana1.withdraw()
        ventanaSalida = tk.Tk()
        ventanaSalida.title("Taller de Mecanica")
        ventanaSalida.geometry("800x600")
        textoSalida = "Hasta pronto"
        etiqueta = tk.Label(ventanaSalida, text=textoSalida, borderwidth=2, relief="solid", wraplength=770, font=16)
        etiqueta.grid(row=0, column=0, padx=10, pady=10)

    def descripcionFunc(self):
        textoDescripcion = "Un Taller es una aplicación de escritorio diseñada para simplificar las tareas administrativas relacionadas con la reparación de automóviles en un taller mecánico."
        etiqueta = tk.Label(self.ventana1, text=textoDescripcion, borderwidth=2, relief="solid", wraplength=770, font=16)
        etiqueta.grid(row=2, column=0, sticky='n', padx=10, pady=10)

    def ingresarFunc(self):
        self.ventana1.withdraw() # Minimiza la ventana inicial
        ventana_principal = tk.Tk()
        app = MiAplicacion(ventana_principal)
        ventana_principal.mainloop()

if __name__ == "__main__":
    VentanaInicial()
    
    
