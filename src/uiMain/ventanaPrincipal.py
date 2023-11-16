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
        self.ventana1.geometry("1500x740")

        # Frame superior
        frame_superior = tk.Frame(self.ventana1)
        frame_superior.pack(fill=tk.X)

        frame_titulo1 = tk.Frame(frame_superior, bg="red", height=50)
        tk.Label(frame_titulo1, text="¡Bienvenid@!", font=("Arial", 14), bg="red", fg="white").pack(fill=tk.BOTH, expand=True)
        frame_titulo1.pack(fill=tk.X)

        # Zona izquierda superior
        frame_izquierda = tk.Frame(frame_superior)
        frame_izquierda.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        texto_breve_descripcion = "Bienvenido al sistema del Taller de Mecanica, en este espacio usted podrá administrar nóminas, inventarios, proveedores y repuestos dependiendo de su categoría de usuario. Garantizamos un acceso seguro y controlado a las diversas funciones y datos del programa"
        etiqueta_izquierda = tk.Label(frame_izquierda, text=texto_breve_descripcion, borderwidth=2, relief="solid", wraplength=700, font=16 )
        etiqueta_izquierda.pack(side=tk.LEFT, pady=12)

        # Barra de menú
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Salir", command=self.salirFunc)
        opciones1.add_command(label="Descripción", command=self.descripcionFunc)
        
        menubar1.add_cascade(label="Inicio", menu=opciones1)

        # Botón "Ingresar"
        b_ingresar = tk.Button(self.ventana1, text="Ingresar", command=self.ingresarFunc)
        b_ingresar.place(width=170, x=250, y=700)

        # Zona derecha superior
        frame_derecha = tk.Frame(frame_superior)
        frame_derecha.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        self.descripcionManu()

        self.ventana1.mainloop()

    def descripcionManu(self):
        bDescripcionManu = tk.Button(self.ventana1, text="Soy Manuela Chaverra, \n tengo 20 años, soy estudiante de ingeniería en sistemas de quinto semestre \n y me gusta jugar futbol y compartir tiempo con mi familia en mi tiempo libre", font = 16, command=self.descripcionAnge)
        bDescripcionManu.place(width=700, x=790, y= 40)
        #faltan las imagenes
    
    def descripcionAnge(self):
        bDescripcionAnge = tk.Button(self.ventana1, text="Soy Angélika Moya, \n tengo 18 años, soy estudiante de ingeniería en sistemas de tercer semestre \n y me gusta jugar futbol y leer en mi tiempo libre", font = 16, command=self.descripcionJero)
        bDescripcionAnge.place(width=700, x=790, y= 40)

    def descripcionJero(self):
        bDescripcionJero = tk.Button(self.ventana1, text="Soy Jerónimo Vásquez, \n tengo 20 años, soy estudiante de ingeniería en sistemas de cuarto semestre \n y me gusta jugar videojuegos en mi tiempo libre", font = 16, command=self.descripcionJuan)
        bDescripcionJero.place(width=700, x=790, y= 40)

    def descripcionJuan(self):
        bDescripcionJuan = tk.Button(self.ventana1, text="Soy Juan Estevan Sinitave, tengo 21 años, estudio ingeniería en sistemas, \nvoy en quinto semestre y me gusta escuchar Hip Hop, \nver series y practicar basketball en mi tiempo libre", font = 16, command=self.descripcionManu)
        bDescripcionJuan.place(width=700, x=790, y= 40)


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
        etiqueta.place(width=740, x=10, y= 160)

    def ingresarFunc(self):
        self.ventana1.withdraw() # Minimiza la ventana inicial
        ventana_principal = tk.Tk()
        app = MiAplicacion(ventana_principal)
        ventana_principal.mainloop()

if __name__ == "__main__":
    VentanaInicial()
    
    
