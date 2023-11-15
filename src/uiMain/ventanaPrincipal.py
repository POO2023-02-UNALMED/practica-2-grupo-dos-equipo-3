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

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = MiAplicacion(ventana_principal)
    ventana_principal.mainloop()
