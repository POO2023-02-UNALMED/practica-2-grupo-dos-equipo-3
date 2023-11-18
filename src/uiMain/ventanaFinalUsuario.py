###ESTE ES EL BUENO
import tkinter as tk

class FieldFrame(tk.Frame):
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__()

        self.criterios = criterios
        self.valores = valores

        # Crear etiquetas y campos usando Grid
        for i, criterio in enumerate(criterios):
            label = tk.Label(self, text=f"{criterio}")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

            if habilitado and habilitado[i] is not None and not habilitado[i]:
                # Campo no editable
                entry = tk.Entry(self, state="disabled")
            else:
                # Campo editable
                entry = tk.Entry(self)

            # Asignar valor inicial si se proporciona
            if valores and valores[i] is not None:
                entry.insert(0, valores[i])

            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")

        # Botones Aceptar y Borrar
        self.boton_aceptar = tk.Button(self, text="Aceptar", command=self.aceptar)
        self.boton_borrar = tk.Button(self, text="Borrar", command=self.borrar)

        self.boton_aceptar.grid(row=len(criterios), column=0, pady=5)
        self.boton_borrar.grid(row=len(criterios), column=1, pady=5)

    def aceptar(self):
        # Guardar los valores en las variables correspondientes
        self.valores = [entry.get() for entry in self.winfo_children() if isinstance(entry, tk.Entry)]
        print("Valores guardados:", self.valores)

    def borrar(self):
        # Poner los valores en blanco o vacío
        for entry in self.winfo_children():
            if isinstance(entry, tk.Entry):
                entry.delete(0, "end")

class VentanaUsuario:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("UNTaller")
        self.ventana1.geometry("500x390")

        self.frame = tk.Frame(self.ventana1, width=400, height=200)
        self.frame.pack(expand=True)

        self.label1 = tk.Label(self.frame, text="¡Bienvenido a UNTAller!", font=("Arial", 16))
        self.label2 = tk.Label(self.frame, text="¿Cuál será tu petición el día de hoy?")
        self.label1.grid(row=0, column=0, padx=20, pady=20, sticky="ns")
        self.label2.grid(row=1, column=0, padx=20, pady=30, sticky="ns")

        self.criterios = ["", "", "", ""]
        self.valores_iniciales = ["", "", "", ""]
        self.habilitado = [False, False, False, False]  # True significa editable, False no editable
        self.frame2 = FieldFrame("Criterio", self.criterios, "Valor", self.valores_iniciales, self.habilitado)
        self.frame2.pack(padx=10, pady=10)

        menubar1 = tk.Menu(self.frame)
        self.ventana1.config(menu=menubar1)

        opciones1 = tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        opciones1.add_command(label="Aplicación", command=self.aplicacion)
        opciones1.add_command(label="Salir", command=self.ventana1.destroy)

        opciones2 = tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="Procesos y Consultas", menu=opciones2)
        opciones2.add_command(label="Solicitar un servicio", command=self.funcionalidad1)
        opciones2.add_command(label="Realizar un servicio", command=self.funcionalidad2)
        opciones2.add_command(label="Solicitar repuestos", command=self.funcionalidad3)
        opciones2.add_command(label="Generar resumen financiero", command=self.funcionalidad4)
        opciones2.add_command(label="Realizar encuesta", command=self.funcionalidad5)

        opciones3 = tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="Ayuda", menu=opciones3)
        opciones3.add_command(label="Acerca de:", command=self.acercaDe)

        self.ventana1.mainloop()

    def aplicacion(self):
        ventanaSalida = tk.Tk()
        ventanaSalida.title("Nosotros")
        ventanaSalida.geometry("725x100")
        textoSalida = "Este programa busca suplir necesidades y simplificar tareas dentro del negocio\n dentro el podrás, llevar a cabo reparaciones, solicitar repuestos,\n administrar la situación financiera del taller y realizar encuestas de satisfacción"
        etiqueta = tk.Label(ventanaSalida, text=textoSalida, borderwidth=2, relief="solid", wraplength=770, font=8)
        etiqueta.grid(row=0, column=0, padx=10, pady=10)

    def acercaDe(self):
        ventanaSalida = tk.Tk()
        ventanaSalida.title("UNTallerAutores")
        ventanaSalida.geometry("470x170")
        textoSalida = "Programa realizado por:\n Manuela Chaverra\n Angelika Moya\n Jeronimo Gonzales\n Juan Sinitave\n En memoria de nuestros compitas que cancelaron"
        etiqueta = tk.Label(ventanaSalida, text=textoSalida, borderwidth=2, relief="solid", wraplength=770, font=16)
        etiqueta.grid(row=0, column=0, padx=10, pady=10)

    def funcionalidad1(self):
        self.label1.config(text="Solicitar un servicio", font=("Arial", 16))
        self.label2.config(text="Ingresa, que deseas hacer hoy")

        criterios_nuevos = ["Nombre", "Vehiculo", "Auto"]
        valores_iniciales_nuevos = ["", "", ""]
        habilitado_nuevos = [True, True, True]

        nuevo_frame2 = FieldFrame("Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

    def funcionalidad2(self):
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
        self.label2.config(text="Mecanico, ¡ingresa los pasos correctos!")

        criterios_nuevos = ["Nombre", "Numero Orden"]
        valores_iniciales_nuevos = ["001", "Producto A"]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame("Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

    def funcionalidad3(self):
        self.label1.config(text="Solicitar repuestos", font=("Arial", 16))
        self.label2.config(text="Dime, ¿que deseas pedir?")

        criterios_nuevos = ["Categoria", "Tipo de daño"]
        valores_iniciales_nuevos = ["Deluxe/Generico", "Producto"]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame("Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

    def funcionalidad4(self):
        self.label1.config(text="Generar resumen financiero", font=("Arial", 16))
        self.label2.config(text="¿Que resumen deseas hacer?\n1)Menos ingresos\n2)Mas ingresos\n3)Total")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame("Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

    def funcionalidad5(self):
        self.label1.config(text="Realizar encuesta", font=("Arial", 16))
        self.label2.config(text="¡Tu opinion nos ayudara a mejorar!")

        criterios_nuevos = ["Nombre", "Mecanico"]
        valores_iniciales_nuevos = ["Raul", "Fernando Miguel"]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame("Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

if __name__ == "__main__":
    VentanaUsuario()


    