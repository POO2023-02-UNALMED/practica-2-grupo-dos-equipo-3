#ESTA ES LA BUENA BUENA 
#BUENA BUENA BUENA

import tkinter as tk



class FieldFrame(tk.Frame):
    def __init__(self, ventana_usuario, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__()

        self.ventana_usuario = ventana_usuario
        self.criterios = criterios
        self.valores = valores
                
        self._clienteCreado = None

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
        ##LA IDEA SERIA ACÄ USAR LOS METODOS Y LO QUE NECESITAMOS CON LOS ID DE CADA FUNCIONALIDAD  CON PUROS CONDICIONALES
        print(self.valores)

        if self.ventana_usuario.idFun == 0:
            self.ventana_usuario.actualizar_label()
        
        ##metan lo suyo en donde va que después nos confundimos todos 
        #los tqm 
        
        ###########todo funcionalidad 1
        elif self.ventana_usuario.idFun == 1:
            self._clienteCreado = self.ventana_usuario.funcionalidad1_1(self.valores)
        
        elif self.ventana_usuario.idFun == 1.1:
            self.ventana_usuario.funcionalidad1_2(self._clienteCreado, self.valores)
        
        ###########todo funcionalidad 2
        elif self.ventana_usuario.idFun == 2:
            self.ventana_usuario.funcionalidad2_1(self.valores[0], self.valores[1])

        elif self.ventana_usuario.idFun == 2.1:
            self.ventana_usuario.funcionalidad2_2(self.valores[0], self.valores[1], self.valores[2], self.valores[3], self.valores[4])
            

        
        ###########todo funcionalidad 3
        elif self.ventana_usuario.idFun == 3:
            self.ventana_usuario.funcionalidad3_1(self.valores[0])
        
        ###########todo funcionalidad 4
        elif self.ventana_usuario.idFun == 4 and self.valores[0] == "1" :
            self.ventana_usuario.funcionalidad4_1()

        elif self.ventana_usuario.idFun == 4.1:
            self.ventana_usuario.funcionalidad4_1Final(self.valores)
                
        elif self.ventana_usuario.idFun == 4 and self.valores[0] == "2" :
            self.ventana_usuario.funcionalidad4_2()

        elif self.ventana_usuario.idFun == 4.2 and self.valores[0] == "1": 
            self.ventana_usuario.funcionalidad4_2Repuestos()

        elif self.ventana_usuario.idFun == 4.2 and self.valores[0] == "2":
            self.ventana_usuario.funcionalidad4_2Mecanicos()

        elif self.ventana_usuario.idFun == 4.21: 
            self.ventana_usuario.funcionalidad4_2RepuestosFinal(self.valores)
        
        elif self.ventana_usuario.idFun == 4.22: 
            self.ventana_usuario.funcionalidad4_2MecanicosFinal(self.valores)
        
        elif self.ventana_usuario.idFun == 4.3:
            self.ventana_usuario.funcionalidad4_3()
        
        ###########todo funcionalidad 5
        elif self.ventana_usuario.idFun == 5:
            self.ventana_usuario.funcionalidad5_1()
        elif self.ventana_usuario.idFun == 5.1:
            self.ventana_usuario.funcionalidad5_2()
        elif self.ventana_usuario.idFun == 5.2:
            self.ventana_usuario.funcionalidad5_3()
        elif self.ventana_usuario.idFun == 5.3:
            self.ventana_usuario.funcionalidad5_4()
        elif self.ventana_usuario.idFun == 5.4:
            self.ventana_usuario.funcionalidad5_5()
        
        
        

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
        self.frame2 = FieldFrame(self, "Criterio", self.criterios, "Valor", self.valores_iniciales, self.habilitado)
        self.frame2.pack(padx=10, pady=10)

        menubar1 = tk.Menu(self.frame)
        self.ventana1.config(menu=menubar1)

        self.idFun = 0
        
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

        criterios_nuevos = ["Nombre", "Vehiculo"]
        valores_iniciales_nuevos = ["Generico/Deluxe",""]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 1

    def funcionalidad1_1(self, valores):
        if not(valores[1] == "Carro" or valores[1] == "Moto"):
            #Error debido a que no se eligio un vehiculo posible
            pass
        
        #cliente = Clientes(valores[0], Vehiculo(valores[1], None))
        
        self.label1.config(text="Solicitar un servicio", font=("Arial", 16))
        self.label2.config(text="Ingresa, que deseas hacer hoy")

        criterios_nuevos = ["Tipo de daño","Nombre mecanico"]
        valores_iniciales_nuevos = ["Motor/Frenos",""]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 1.1
        return None#cliente

    def funcionalidad1_2(self, cliente, valores):
        cliente.getVehiculos()[0].setTipoDeDanio(valores[0], None) #setTipoDeDanio(valores[0], admin)
        
        self.label2.config(text="Repuestos disponibles: \n")

        
    def funcionalidad2(self):
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
        self.label2.config(text="Mecanico, identificate y escribe el numero de orden que quieres realizar")

        criterios_nuevos = ["Nombre", "Numero Orden"]
        valores_iniciales_nuevos = ["", ""]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 2

    def funcionalidad2_1(self, nombreMecanico, numeroOrden):
        """falta describir la orden"""
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
        self.label2.config(text=nombreMecanico +", de acuerdo a la descripcion de la orden ingresa los pasos correctos\n"+numeroOrden)

        criterios_nuevos = ["primer numero", "segundo numero", "tercer numero", "cuarto numero", "quinto numero"]
        valores_iniciales_nuevos = ["", "", "", "", ""]
        habilitado_nuevos = [True, True, True, True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 2.1
        
    def funcionalidad2_2(self, val1, val2, val3, val4, val5):
        # Cambiar el orden para configurar las etiquetas después de destruir y recrear el frame
        print("valor 1 "+ val1 + " |valor2 "+ val2 +" |valor3 "+ val3 +" |valor4 "+ val4 + " |valor5 "+val5 )
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
        correcto = "12345"
        if val1 + val2 + val3 + val4 + val5 == correcto:
            self.label2.config(text="usted ha ganado -5000-\n ha reparado el vehiculo ¿le gustaria hacer algo más?")
            criterios_nuevos = ["1.Consultar ordenes realizadas", "2.Consultar comisiones"]
            valores_iniciales_nuevos = ["si/no", "si/no"]
            habilitado_nuevos = [True, True]
            nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

            self.frame2.destroy()
            self.frame2 = nuevo_frame2
            self.frame2.pack(padx=10, pady=10)
        else:
            self.label2.config(text="se ha equivocado en el orden de los pasos y ha generado un error de tipo -carroceria-\nintentelo de nuevo")
            self.funcionalidad2_21()

    def funcionalidad2_21(self):
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
        #self.label2.config(text=nombreMecanico +", de acuerdo a la descripcion de la orden ingresa los pasos correctos\n"+numeroOrden)

        criterios_nuevos = ["primer numero", "segundo numero", "tercer numero", "cuarto numero", "quinto numero"]
        valores_iniciales_nuevos = ["", "", "", "", ""]
        habilitado_nuevos = [True, True, True, True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        

    def funcionalidad3(self):
        self.label1.config(text="Solicitar repuestos", font=("Arial", 16))
        self.label2.config(text="Dime, ¿que deseas pedir?")

        criterios_nuevos = ["Categoria", "Tipo de daño"]
        valores_iniciales_nuevos = ["Deluxe/Generico", "Producto"]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 3
        
    def funcionalidad3_1(self, categoriaDada):
        self.label1.config(text="Solicitar repuestos", font=("Arial", 16))
        
        respuestosD = ""
        indice = 1
        if categoriaDada == "Deluxe":
            #llenar respuestosD con admin
            pass
        elif categoriaDada == "Generico":
            #llenar respuestosD con admin
            pass
        
        self.label2.config(text="Escoja respuestos: " + respuestosD)
        
        criterios_nuevos = ["Repuesto", "Proveedor"]
        valores_iniciales_nuevos = ["", ""]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
            
        
    def funcionalidad4(self):
        self.label1.config(text="Generar resumen financiero", font=("Arial", 16))
        self.label2.config(text="¿Que resumen deseas hacer?\n1)Menos ingresos\n2)Mas ingresos\n3)Total")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 4

    def funcionalidad4_1(self):
        #Logica para encontrar el servicio con mas ingresos
        self.label2.config(text="El resultado con mas ingresos fue:\n Ingresa el valor de comisión \nque deseas dar a los mecanicos \nen caso tal")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.1

    def funcionalidad4_1Final(self, valores):
        self.frame2.destroy()
        self.label2.config(text=f"Le has subido el precio a los repuestos en:\n{valores[0]} unidades")
    
    def funcionalidad4_2(self):
        #Lógica para obtener el servicio con menos ingresos 
        self.label2.config(text="El servicio con menos ingresos fue:\n ¿que deseas hacer?\n1)Aumentar precio repuestos\n2)Disminuir comisiones a los mecanicos")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.2

    def funcionalidad4_2Repuestos(self):
        #Lógica para aumentar el precio de los repuestos
        self.label2.config(text="En cuanto desea aumentar el precio de los repuestos?")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.21
    
    def funcionalidad4_2RepuestosFinal(self, valores):
        self.frame2.destroy()
        self.label2.config(text=f"Le has subido el precio a los repuestos en:\n{valores[0]} unidades")

    def funcionalidad4_2Mecanicos(self):
        #Lógica para disminuir comision de los mecanicos
        self.label2.config(text="En cuanto desea disminuir la comisión de los mecanicos?")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.22
    
    def funcionalidad4_2MecanicosFinal(self, valores):
        self.frame2.destroy()
        self.label2.config(text=f"Le has diminuido la comision a los mecanicos en:\n{valores[0]} unidades")
    

    def funcionalidad4_3(self):
        self.frame2.destroy()
        admin.finanzas()
        
        self.label2.config(text=f"Este es el resumen general de su taller:\n "
                       f"Cartera final: {admin.getInventario().getCartera_inicial()}\n "
                       f"Gastos: {admin.getInventario().getGastos()}\n "
                       f"Ingresos: {admin.getInventario().getIngresos()}\n "
                       f"Numero de Ordenes: {admin.numOrdenes()}\n "
                       f"Numero de mecanicos: {admin.getMecanicos().size()}\n "
                       f"Servicio menos rentable: {admin.ordenMasRentable()}\n "
                       f"Servicio mas rentable: {admin.ordenMenosRentable()} \n "
                       f"Calificación del taller: {admin.getCalificacionTaller()}")

        
        
        self.idFun = 4.3
        

    def funcionalidad5(self):
        self.label1.config(text="Realizar encuesta", font=("Arial", 16))
        self.label2.config(text="¡Tu opinion nos ayudara a mejorar!")

        criterios_nuevos = ["Nombre", "Mecanico"]
        valores_iniciales_nuevos = ["Raul", "Fernando Miguel"]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 5

    def funcionalidad5_1(self):
        self.label1.config(text=f"Gracias por haber \nrealizado un servicio con nosotros!")
        self.label2.config(text="Del 1 al 5 que tal calificas nuestro servicio?")

        criterios_nuevos = ["Calificación"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 5.1

    def funcionalidad5_2(self):
        self.label1.config(text=f"Siempre nos aseguramos \nde usar los repuestos de mayor calidad!")
        self.label2.config(text="Del 1 al 5 que tal calificas nuestros repuestos?")

        criterios_nuevos = ["Calificación"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 5.2
    
    def funcionalidad5_3(self):
        self.label1.config(text=f"Nuestro objetivo es tener el\n personal más capacitado del mercado!")
        self.label2.config(text="Del 1 al 5 que tal calificas el mecánico que te atendió?")

        criterios_nuevos = ["Calificación"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 5.3
    
    def funcionalidad5_4(self):
        self.label1.config(text="Gracias por realizar esta encuesta!")
        self.label2.config(text="Deseas dar una comisión extra al mecanico que te atendió?")

        criterios_nuevos = ["Comisión"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 5.4

    def funcionalidad5_5(self):
        self.frame2.destroy()
        self.label1.config(text="Muchas gracias!")
        self.label2.config(text="Esperamos que vuelvas pronto")

    
   

    
        

    def actualizar_label(self):
        self.label2.config(text="Por favor, selecciona una consulta para comenzar", font=("Arial", 10))

        

if __name__ == "__main__":
    VentanaUsuario()