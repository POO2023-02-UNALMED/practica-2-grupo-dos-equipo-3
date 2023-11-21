import tkinter as tk
from src.gestorAplicacion.tallerMecanica.Orden import Orden

from src.uiMain.ventanaError import ventanaError
from src.gestorAplicacion.cliente.Clientes import Clientes
from src.gestorAplicacion.cliente.Vehiculo import Vehiculo
from src.gestorAplicacion.cliente.TipoDaño import TipoDaño
from src.gestorAplicacion.tallerMecanica.Administrador import Administrador
from src.gestorAplicacion.tallerMecanica.Mecanicos import Mecanicos
from src.gestorAplicacion.tallerMecanica.Proveedor import Proveedor
from src.gestorAplicacion.tallerMecanica.RepuestosGenericos import RepuestosGenericos
from src.gestorAplicacion.tallerMecanica.RepuestosDeluxe import RepuestosDeluxe
from src.gestorAplicacion.tallerMecanica.Inventario import Inventario
from src.baseDatos.serializador import serializador
from src.errores.errorCasillasVacias import ErrorCasillasVacias
from src.errores.errorVElejido import ErrorVehiculoElejido
from src.errores.errorNone import ErrorNoOrdenes,ErrorClienteNone,ErrorMecanicoNone
from src.errores.errorTipoDato import ErrorDato
from src.uiMain.ventanaError import ventanaError
from src.errores.errorRepElejido import ErrorRepuestoElejido
from src.errores.ErrorCatElejida import ErrorCategoriaElejido


admin = Administrador()

mecanico1 = Mecanicos("Jeronimo", "Carro", admin)
mecanico2 = Mecanicos("Juan", "Moto", admin)
mecanico3 = Mecanicos("Manuela", "Carro", admin)
mecanico4 = Mecanicos("Angelika", "Moto", admin)
mecanico5 = Mecanicos("Fernando Miguel", "Carro", admin)
mecanicos = [mecanico1,mecanico2,mecanico3,mecanico4,mecanico5]

repuestoGenerico1 = RepuestosGenericos()
repuestoGenerico1.setRepuestosMotor([['Bujia', 2, 3000], ['Filtro de aceite', 2, 2010]]) 
repuestoGenerico1.setRepuestosFrenos([['Pastilla de frenos', 2, 1990], ['Liquido de frenos', 2, 2030]]) 
repuestoGenerico1.setRepuestosElectrico([['Bateria', 2, 4567], ['Focoss', 2, 2230]])
repuestoGenerico1.setRepuestosLlantas([['Valvula', 2, 1234], ['Tapa de la valvula', 2, 6872]])
repuestoGenerico1.setRepuestosCarroceria([['Pintura', 2, 4103], ['Espejos', 2, 7891]])

repuestoDeluxe1 = RepuestosDeluxe()
repuestoDeluxe1.setRepuestosMotor([['Bujia', 2, 4050], ['Filtro de aceite', 2, 3110]]) 
repuestoDeluxe1.setRepuestosFrenos([['Pastilla de frenos', 2, 3900], ['Liquido de frenos', 2, 2990]]) 
repuestoDeluxe1.setRepuestosElectrico([['Bateria', 2, 5600], ['Focoss', 2, 4220]])
repuestoDeluxe1.setRepuestosLlantas([['Valvula', 2, 4203], ['Tapa de la valvula', 2, 8980]])
repuestoDeluxe1.setRepuestosCarroceria([['Pintura', 2, 5600], ['Espejos', 2, 9870]])

proveedor1 = Proveedor("Stuar Little", admin, 123, repuestoDeluxe1, repuestoGenerico1)
repuestoDeluxe1.setProveedor(proveedor1)
repuestoGenerico1.setProveedor(proveedor1)

repuestoGenerico2 = RepuestosGenericos()
repuestoGenerico2.setRepuestosMotor([['Bujia', 2, 3450], ['Filtro de aceite', 2, 5600]]) 
repuestoGenerico2.setRepuestosFrenos([['Pastilla de frenos', 3402, 0], ['Liquido de frenos', 2, 6200]]) 
repuestoGenerico2.setRepuestosElectrico([['Bateria', 2, 1203], ['Focoss', 2, 2304]])
repuestoGenerico2.setRepuestosLlantas([['Valvula', 2, 5870], ['Tapa de la valvula', 2, 5060]])
repuestoGenerico2.setRepuestosCarroceria([['Pintura', 2, 2035], ['Espejos', 2, 6093]])

repuestoDeluxe2 = RepuestosDeluxe()
repuestoDeluxe2.setRepuestosMotor([['Bujia', 2, 4205], ['Filtro de aceite', 2, 7600]]) 
repuestoDeluxe2.setRepuestosFrenos([['Pastilla de frenos', 2, 5406], ['Liquido de frenos', 2, 8980]]) 
repuestoDeluxe2.setRepuestosElectrico([['Bateria', 2, 2400], ['Focoss', 2, 4950]])
repuestoDeluxe2.setRepuestosLlantas([['Valvula', 2, 7899], ['Tapa de la valvula', 2, 0]])
repuestoDeluxe2.setRepuestosCarroceria([['Pintura', 2, 3053], ['Espejos', 2, 8999]])

proveedor2 = Proveedor("Bad Bunny", admin, 321, repuestoDeluxe2, repuestoGenerico2)
repuestoDeluxe1.setProveedor(proveedor2)
repuestoGenerico1.setProveedor(proveedor2)

proveedores = [proveedor1, proveedor2]

deluxeInventario = RepuestosDeluxe()
deluxeInventario.setRepuestosMotor([['Bujia', 2, 5060], ['Filtro de aceite', 2, 7080]]) 
deluxeInventario.setRepuestosFrenos([['Pastilla de frenos', 2, 8880], ['Liquido de frenos', 2, 6700]]) 
deluxeInventario.setRepuestosElectrico([['Bateria', 2, 11230], ['Focoss', 2, 9394]])
deluxeInventario.setRepuestosLlantas([['Valvula', 2, 5031], ['Tapa de la valvula', 2, 7893]])
deluxeInventario.setRepuestosCarroceria([['Pintura', 2, 6707], ['Espejos', 2, 9877]])

genericoInventario = RepuestosGenericos()
genericoInventario.setRepuestosMotor([['Bujia', 2, 4506], ['Filtro de aceite', 2, 6705]]) 
genericoInventario.setRepuestosFrenos([['Pastilla de frenos', 2, 6089], ['Liquido de frenos', 2, 5980]]) 
genericoInventario.setRepuestosElectrico([['Bateria', 2, 8999], ['Focoss', 2, 8971]])
genericoInventario.setRepuestosLlantas([['Valvula', 2, 4560], ['Tapa de la valvula', 2, 5697]])
genericoInventario.setRepuestosCarroceria([['Pintura', 2, 5697], ['Espejos', 2, 7812]])

inventario = Inventario(admin, deluxeInventario ,genericoInventario)

motor = TipoDaño("Motor")
frenos = TipoDaño("Frenos")
electrico = TipoDaño("Electrico")
llantas = TipoDaño("Llantas")
carroceria = TipoDaño("Carroceria")

admin.añadirTipoDaño(motor)
admin.añadirTipoDaño(frenos)
admin.añadirTipoDaño(electrico)
admin.añadirTipoDaño(llantas)
admin.añadirTipoDaño(carroceria)

admin.setNombre("Julieta Vanegas")
admin.setId(1006784599)
admin.setMecanicos(mecanicos)
admin.setProveedores(proveedores)
admin.setInventario(inventario)
admin.setMecanicos(mecanicos)

class FieldFrame(tk.Frame):
    def __init__(self, ventana_usuario, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__()

        self.ventana_usuario = ventana_usuario
        self.criterios = criterios
        self.valores = valores
                
        self._clienteCreado = None
        self._repuesto =""
        self._vehiculo = ""
        self._categoria = ""
        self._mecanico = ""
        self._clienteCalificando = ""
        self._mecanicoCalificado = ""

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
            try:
                for i in self.valores:
                    if i == "":
                        raise ErrorCasillasVacias()
                
                self._vehiculo = self.valores[2]
                self._categoria = self.valores[1]
                self._mecanico == self.valores[4]
                try:
                    self._clienteCreado = self.ventana_usuario.funcionalidad1_1(self.valores)
                except ErrorVehiculoElejido as v:
                    ventanaError(v.display())
            except ErrorCasillasVacias as f:
                ventanaError(f.display())
        
        elif self.ventana_usuario.idFun == 1.1:
            try:
                self.ventana_usuario.funcionalidad1_2(self.valores)
            except ErrorRepuestoElejido as f:
                ventanaError(f.display())
        
        ###########todo funcionalidad 2
        elif self.ventana_usuario.idFun == 2:
            try:
                for i in self.valores:
                    if i == "":
                        raise ErrorCasillasVacias()
                self.ventana_usuario.funcionalidad2_1(self.valores[0], self.valores[1])
            except ErrorCasillasVacias as f:
                ventanaError(f.display())

        elif self.ventana_usuario.idFun == 2.1:
            self.ventana_usuario.funcionalidad2_2(self.valores[0], self.valores[1], self.valores[2], self.valores[3], self.valores[4])

        elif self.ventana_usuario.idFun == 2.3:
            self.ventana_usuario.funcionalidad2_3(self.valores[0], self.valores[1])

        elif self.ventana_usuario.idFun == 2.4:
            self.ventana_usuario.funcionalidad2_4Final()     

        ###########todo funcionalidad 3
        elif self.ventana_usuario.idFun == 3:
            try:
                for i in self.valores:
                    if i == "":
                        raise ErrorCasillasVacias()
                if not(self.valores[0] == "Deluxe" or self.valores[0] == "Generico"):
                    raise ErrorCategoriaElejido()
                else:
                    repuestos = []
                    respuestosD = ""
                    indice = 1
                    if self.valores[0] == "Deluxe":
                        for i in range(len(admin.getInventario().getRepuestosDeluxe().repuestosDisponibles(self.valores[1]))):
                            repuestos = admin.getInventario().getRepuestosDeluxe().repuestosDisponibles(self.valores[1])
                        
                    elif self.valores[0] == "Generico":
                        for i in range(len(admin.getInventario().getRepuestosGenericos().repuestosDisponibles(self.valores[1]))):
                            repuestos = admin.getInventario().getRepuestosGenericos().repuestosDisponibles(self.valores[1])
                    
                    for rep in repuestos:
                        respuestosD += f"{indice}.{rep}\n"
                        indice += 1
                    self.ventana_usuario.funcionalidad3_1(self.valores, respuestosD)
            except ErrorCasillasVacias as f:
                ventanaError(f.display())
            except ErrorCategoriaElejido as v:
                ventanaError(v.display())
            
        elif self.ventana_usuario.idFun == 3.1:
            try:
                for i in self.valores:
                    if i == "":
                        raise ErrorCasillasVacias()
                self.ventana_usuario.funcionalidad3_2(self.valores)
            except ErrorCasillasVacias as f:
                ventanaError(f.display())
              
        ###########todo funcionalidad 4
        elif self.ventana_usuario.idFun == 4 and self.valores[0] == "1" :
            self.ventana_usuario.funcionalidad4_1()

        elif self.ventana_usuario.idFun == 4 and self.valores[0] == '':      
            try: 
                if self.valores[0] == '':
                    raise ErrorCasillasVacias()
            except ErrorCasillasVacias as a:
                ventanaError(a.display())

        elif self.ventana_usuario.idFun == 4.2 and self.valores[0] == '':
            try:
                if self.valores[0] == '':
                    raise ErrorCasillasVacias()
            except ErrorCasillasVacias as a:
                ventanaError(a.display())

        
        elif self.ventana_usuario.idFun == 4.1:
            try:
                if self.valores[0] == '':
                    raise ErrorCasillasVacias()
                self.ventana_usuario.funcionalidad4_1Final(self.valores)
            except ErrorCasillasVacias as a:
                ventanaError(a.display())
            except ValueError as b:
                raise ErrorDato()
            except ErrorDato as c:
                ventanaError(c.display())
            
            
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
        
        elif self.ventana_usuario.idFun == 4 and self.valores[0] == "3":
            self.ventana_usuario.funcionalidad4_3()
        
        ###########todo funcionalidad 5
        elif self.ventana_usuario.idFun == 5:
            try:
                for valor in self.valores:
                    if valor == '':
                        raise ErrorCasillasVacias()
                self._clienteCalificando = admin.getClienteNombre(self.valores[0])
                self._mecanicoCalificado = admin.asignarMecanico(self.valores[1])
                if self._clienteCalificando == None:
                    raise ErrorClienteNone()
                if self._mecanicoCalificado == None:
                    raise ErrorMecanicoNone()
                self.ventana_usuario.funcionalidad5_1()
            except ErrorClienteNone as e:
                ventanaError(e.display())
            except ErrorMecanicoNone as b:
                ventanaError(b.display())
            except ErrorCasillasVacias as c:
                ventanaError(c.display())
        elif self.ventana_usuario.idFun == 5.1:
            try:
                if self.valores[0] == '':
                    raise ErrorCasillasVacias()
                calificacion = int(self.valores[0])
                self._clienteCalificando.calificarTaller(admin, calificacion)
                self.ventana_usuario.funcionalidad5_2()
            except ErrorCasillasVacias as a:
                ventanaError(a.display())
            except ValueError as b:
                raise ErrorDato()
            except ErrorDato as c:
                ventanaError(c.display())
        elif self.ventana_usuario.idFun == 5.2:
            try:
                if self.valores[0] == "":
                    raise ErrorCasillasVacias()
                calificacion = int(self.valores[0])

                if calificacion < 0:
                    raise ErrorDato()
                if calificacion > 3:
                    admin.getInventario().getRepuestosDeluxe().aumentarPrecio(500,"Motor")
                    admin.getInventario().getRepuestosDeluxe().aumentarPrecio(500,"Frenos")
                    admin.getInventario().getRepuestosDeluxe().aumentarPrecio(500,"Electrico")
                    admin.getInventario().getRepuestosDeluxe().aumentarPrecio(500,"Llantas")
                    admin.getInventario().getRepuestosDeluxe().aumentarPrecio(500,"Carroceria")

                    admin.getInventario().getRepuestosGenericos().aumentarPrecio(500,"Motor")
                    admin.getInventario().getRepuestosGenericos().aumentarPrecio(500,"Frenos")
                    admin.getInventario().getRepuestosGenericos().aumentarPrecio(500,"Electrico")
                    admin.getInventario().getRepuestosGenericos().aumentarPrecio(500,"Llantas")
                    admin.getInventario().getRepuestosGenericos().aumentarPrecio(500,"Carroceria")
                self.ventana_usuario.funcionalidad5_3()
            
            except ErrorCasillasVacias as a:
                ventanaError(a.display())
            except ValueError as b:
                raise ErrorDato()
            except ErrorDato as c:
                ventanaError(c.display())



            
        elif self.ventana_usuario.idFun == 5.3:
            try:
              if self.valores[0] == "":
                  raise ErrorCasillasVacias()
              
              calificacion = int(self.valores[0])
              if self.valores[0] > 3:
                self._mecanicoCalificado.recibirComision(1000)
              self.ventana_usuario.funcionalidad5_4()
            except ErrorCasillasVacias as a:
                ventanaError(a.display())
            except ValueError as b:
                raise ErrorDato()
            except ErrorDato as c:
                ventanaError(c.display())

            
        elif self.ventana_usuario.idFun == 5.4:
            try:
                if self.valores[0] == "":
                    raise ErrorCasillasVacias()
                comision = int(self.valores[0])
           
                self._mecanicoCalificado.recibirComision(comision)
                self._clienteCalificando.pagar(comision)
                self.ventana_usuario.funcionalidad5_5()
            
            except ErrorCasillasVacias as a:
                ventanaError(a.display())
            except ValueError as b:
                raise ErrorDato()
            except ErrorDato as c:
                ventanaError(c.display())
        
        
        
        
        

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
        self.label1.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        self.label2.grid(row=1, column=0, padx=20, pady=10, sticky="n")

        self.criterios = ["", "", "", ""]
        self.valores_iniciales = ["", "", "", ""]
        self.habilitado = [False, False, False, False]  # True significa editable, False no editable
        self.frame2 = FieldFrame(self, "Criterio", self.criterios, "Valor", self.valores_iniciales, self.habilitado)
        self.frame2.pack(padx=10, pady=5, expand = True)

        menubar1 = tk.Menu(self.frame)
        self.ventana1.config(menu=menubar1)

        self.idFun = 0
        self._cliente = None
        self._vehiculo = ""
        self._tipoRep = ""
        self._categoria = ""
        self._mecanico = ""
        self._repuestosD = ""
        
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

    def mostrarError(self, texto):
        self.label2.config(text=texto)
    
    def funcionalidad1(self):
        self.label1.config(text="Solicitar un servicio", font=("Arial", 16))
        self.label2.config(text="Ingresa, que deseas hacer hoy")

        criterios_nuevos = ["Nombre cliente","Categoria", "Vehiculo", "TipoDaño", "Mecanico"]
        valores_iniciales_nuevos = ["","Generico/Deluxe","","Motor/Frenos/...",""]
        habilitado_nuevos = [True,True, True, True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 1

    def funcionalidad1_1(self, valores):
        if not(valores[2] == "Carro" or valores[2] == "Moto"):
            #Error debido a que no se eligio un vehiculo posible
            return
        self._categoria = valores[1]
        self._vehiculo = valores[2]
        self._tipoRep = valores[3]
        self._mecanico = valores[4]
        
        cliente = Clientes(valores[0], Vehiculo(valores[2], None))
        cliente.getVehiculos()[0].setTipoDeDanio(valores[3], admin)
        repuestos = ""
        id = 1
        lista = admin.getInventario().consultarRepuestosDisponibles(valores[1],valores[3])
        self._repuestosD = lista
        
        for rep in lista:
            repuestos += f"{id}.{rep}"
            id += 1
        
        self.label2.config(text="Repuestos disponibles: " + repuestos)
        

        criterios_nuevos = ["Repuesto"]
        valores_iniciales_nuevos = ["(Nombre del repuesto)"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 1.1
                
        self._cliente = cliente
        return cliente       
        
    def funcionalidad1_2(self, valores):
        #try:
            print(admin.getInventario().getRepuestosDeluxe().obtenerPrecio('Motor','Bujia'))
            for i in self._repuestosD:
                if i == valores[0]:
                    precio = 0
                if (self._vehiculo == "Moto" and self._categoria == "Deluxe"):
                    precio = admin.getInventario().getPrecioMoto() + admin.getInventario().getRepuestosDeluxe().obtenerPrecio(tiporepuesto=self._tipoRep, repuesto=valores[0])

                elif (self._vehiculo == "Carro" and self._categoria == "Deluxe"):
                    precio = admin.getInventario().getPrecioCarro() + admin.getInventario().getRepuestosDeluxe().obtenerPrecio(tiporepuesto=self._tipoRep, repuesto=valores[0])
                                            
                elif(self._categoria == "Generico" and self._vehiculo == "Moto"):
                    precio = admin.getInventario().getPrecioMoto() + admin.getInventario().getRepuestosGenericos().obtenerPrecio(tiporepuesto=self._tipoRep, repuesto=valores[0])
                                            
                elif (self._vehiculo == "Carro" and self._categoria == "Generico"):
                    precio = admin.getInventario().getPrecioCarro() + admin.getInventario().getRepuestosGenericos().obtenerPrecio(tiporepuesto=self._tipoRep, repuesto=valores[0])

                print(self._cliente)
                orden = self._cliente.crearOrden(self._cliente.getVehiculos()[0], self._mecanico, admin, precio)
                orden.setRepuesto(valores[0])
                print(orden)
                
                self.frame2.destroy()
                self.label2.config(text="Precio: "+precio)
            #else:
                #raise ErrorRepuestoElejido()
        #except:
            #raise ErrorRepuestoElejido()
        
    def funcionalidad2(self):
        "no se ingresa ningun nombre de mecanico ni ninguna orden "
        mecanicos_text = ""
        ordenes_text = ""
        mecanico = None

        nombre_mecanico = ""  

        for i in range(len(admin.mecanicosTrabajando())):
            mecanicos_text += f"{i}.{admin.mecanicosTrabajando()[i].getNombre()}\n"

        self.label2.config(text=mecanicos_text + "Hola mecanico ¿Cuál es tu nombre?")

        self.label1.config(text="Realizar servicio", font=("Arial", 16))

        criterios_nuevos = ["Nombre", "Numero Orden"]
        valores_iniciales_nuevos = ["", ""]
        habilitado_nuevos = [True, True]

        for m in admin.mecanicosTrabajando():
            if m.getNombre() == nombre_mecanico:
                mecanico = m
                break

        if mecanico is not None:
            for i in range(len(mecanico.getOrdenes())):
                ordenes_text += f"{i}.Orden{i}"

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 2


    def funcionalidad2_1(self, nombreMecanico, numeroOrden):
        """falta insertar bien la orden para saber que combinacion es la correcta"""
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
        "no falta nada "
        print("valor 1 "+ val1 + " |valor2 "+ val2 +" |valor3 "+ val3 +" |valor4 "+ val4 + " |valor5 "+val5 )
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
        correcto = "12345"
        if val1 + val2 + val3 + val4 + val5 == correcto:
            self.label2.config(text="usted ha ganado -5000-\n ha reparado el vehiculo ¿le gustaria hacer algo más?")
            criterios_nuevos = ["1.Consultar ordenes realizadas", "2.Consultar comisiones"]
            valores_iniciales_nuevos = ["", ""]
            habilitado_nuevos = [True, True]
            nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

            self.frame2.destroy()
            self.frame2 = nuevo_frame2
            self.frame2.pack(padx=10, pady=10)
            #self.funcionalidad2_3(self.valores_iniciales[0], valores_iniciales_nuevos[1])
            self.idFun = 2.3
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
    
    def funcionalidad2_3(self, ordenes, comisiones):
        """En esta funcionalidad falla el uso de los if, falta modificar"""
       
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
    
        if ordenes == "'si'" and comisiones == "'no'":
            self.label2.config(text="aqui deben ir los id de las ordenes realizadas")
        else:
            self.label2.config(text="Hasta luego" + " ordenes: "+ordenes + " |comisiones: "+ comisiones) 
            self.idFun= 2.4

        if ordenes == "'no'" and comisiones == "'si'":
            self.label2.config(text="aqui debe ir la comision" +" ordenes: "+ordenes + " |comisiones: "+ comisiones)
        else:
            self.label2.config(text="Hasta luego" + ordenes + comisiones)
            self.idFun= 2.4

        if ordenes == "'si'" and comisiones == "'si'":
            self.label2.config(text="aqui deben ir los id de las ordenes realizadas y la comision")
        else:
            self.label2.config(text="Hasta luego" + "ordenes: "+ordenes + " |comisiones**: "+ comisiones)
            self.idFun=2.4

    def funcionalidad2_4Final(self):
        #criterios_nuevos = None
        #valores_iniciales_nuevos = None
        #habilitado_nuevos = None
        #nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)
        #self.frame2.destroy()
        #self.frame2 = nuevo_frame2
        #self.frame2.pack(padx=10, pady=10)
        
        self.label1.config(text="Realizar servicio", font=("Arial", 16))
    
        self.label2.config(text="Hasta luego")
        

    def funcionalidad3(self):
        self.label1.config(text="Solicitar repuestos", font=("Arial", 16))
        self.label2.config(text="Dime, ¿que deseas pedir?")

        criterios_nuevos = ["Categoria", "Tipo de daño"]
        valores_iniciales_nuevos = ["Deluxe/Generico", "Producto", ]
        habilitado_nuevos = [True, True,]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 3
        
    def funcionalidad3_1(self, valores, repuestosD):
        self._tipoRep = valores[0]
        self._categoria = valores[1]
        self.label1.config(text="Solicitar repuestos", font=("Arial", 16))
        
        
        self.label2.config(text="Escoja respuestos: \n" + repuestosD)
        
        criterios_nuevos = ["Repuesto", "Proveedor"]
        valores_iniciales_nuevos = ["(Nombre repuesto)", ""]
        habilitado_nuevos = [True, True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 3.1
        
    def funcionalidad3_2(self, valores):
        self.frame2.destroy()
        precio = 0
        proveedor_lista = []
        if(self._tipoRep == "Deluxe"):		
            for i in range(len(admin.proveedoresDisponiblesRepuestosDeluxe(self._categoria, valores[0]))):         							
                proveedor_lista = admin.proveedoresDisponiblesRepuestosDeluxe(self._categoria, valores[0])
            precio = proveedor_lista[0].getRepuestosDeluxe().obtenerPrecio(self._tipoRep, valores[0])
        elif (self._tipoRep == "Generico"):    						
            for i in range(len(admin.proveedoresDisponiblesRepuestosGenerico(self._categoria,valores[0]))):
                proveedor_lista = admin.proveedoresDisponiblesRepuestosGenerico(self._categoria,valores[0])
            precio = proveedor_lista[0].getRepuestosDeluxe().obtenerPrecio(self._tipoRep, valores[0])
        
        cantidad = 1
        try:
            orden_repuesto = Orden("Repuestos", precio)
            orden_repuesto.setRepuesto(valores[0])
            
            admin.solicitarRepuestos(categoria=self._categoria,tipo=self._tipoRep, repuesto=valores[0], cantidad=cantidad, proveedor_nombre=valores[1])
            admin.getInventario().pagar(precio)
            self.label2.config(text="Solicitud exitosa")
        except Exception as e:
            print(e)
	            				
    def funcionalidad4(self):
        self.label1.config(text="Generar resumen financiero", font=("Arial", 16))
        self.label2.config(text="¿Que resumen deseas hacer?\n1)Servicio que genera mas ingresos\n2)Servicio que genera menos ingresos \n3)Total")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["1/2/3"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)

        self.idFun = 4

    def funcionalidad4_1(self):
        print(len(admin._ordenes))
        if len(admin._ordenes) == 0:
            self.label1.config(text="Aún no se ha ejecutado ninguna orden \npero le pudes dar un apoyo a tus mecanicos :)", font=("Arial", 16))
        else:
            self.label1.config(text=f"La orden mas rentable del taller ha sido: \n{admin.ordenMasRentable()}", font=("Arial", 16))
        print(admin.ordenMasRentable())
        self.label2.config(text="\n Ingresa el valor de comisión en bonificación \nque deseas dar a los mecanicos. \nEn caso tal de no desear tal aumento ingrese 0")

        criterios_nuevos = ["Bonificación"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.1

    def funcionalidad4_1Final(self, valores):
        self.frame2.destroy()
        
        if valores[0] == "0": 
            self.label2.config(text=f"por favor selecciona una nueva petición en el menú de arriba")
            self.label1.config(text=f"Esperamos pronto haga una nueva consulta :)", font=("Arial",16))
            
        else:
            comision = int(valores[0])
            mecanicosAumentar = list()
            if admin.ordenMasRentable() == "Reparación de Carros":
               mecanicosAumentar = admin.obtenerMecanicosAfines("Carro")
        
            elif admin.ordenMasRentable() == "Reparación de Motos":
                mecanicosAumentar = admin.obtenerMecanicosAfines("Moto")
        
            for i in mecanicosAumentar:
                mecanicosAumentar[i].recibirComision(comision)

            self.label2.config(text=f"Le has dado un aumento de comisión a los mecanicos en:\n{valores[0]} unidades")



    def funcionalidad4_2(self):
        if len(admin._ordenes) == 0:
            self.label1.config(text="Aún no se ha ejecutado ninguna orden \npero puedes prevenir", font=("Arial", 16))
            self.label2.config(text="¿Que deseas hacer?\n1)Aumentar precio repuestos\n2)Disminuir comisiones a los mecanicos")
        else:
            self.label2.config(text="El servicio con menos ingresos fue:\n ¿que deseas hacer?\n1)Aumentar precio repuestos\n2)Disminuir comisiones a los mecanicos")

        criterios_nuevos = ["Elección"]
        valores_iniciales_nuevos = ["1/2"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.2

    def funcionalidad4_2Repuestos(self):
        #Lógica para aumentar el precio de los repuestos
        self.label2.config(text="En cuanto desea aumentar el precio de los repuestos?")

        criterios_nuevos = ["Aumento"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.21
    
    def funcionalidad4_2RepuestosFinal(self, valores):
        self.frame2.destroy()
        aumento = int(valores[0])
        admin.getInventario().getRepuestosDeluxe().aumentarPrecio(aumento, "Motor")
        admin.getInventario().getRepuestosDeluxe().aumentarPrecio(aumento, "Frenos")
        admin.getInventario().getRepuestosDeluxe().aumentarPrecio(aumento, "Electrico")
        admin.getInventario().getRepuestosDeluxe().aumentarPrecio(aumento, "Llantas")
        admin.getInventario().getRepuestosDeluxe().aumentarPrecio(aumento, "Carroceria")
        admin.getInventario().getRepuestosGenericos().aumentarPrecio(aumento, "Motor")
        admin.getInventario().getRepuestosGenericos().aumentarPrecio(aumento, "Frenos")
        admin.getInventario().getRepuestosGenericos().aumentarPrecio(aumento, "Electrico")
        admin.getInventario().getRepuestosGenericos().aumentarPrecio(aumento, "Llantas")
        admin.getInventario().getRepuestosGenericos().aumentarPrecio(aumento, "Carroceria")
        
        self.label2.config(text=f"Le has subido el precio a los repuestos en:\n{valores[0]} unidades")

    def funcionalidad4_2Mecanicos(self):
        #Lógica para disminuir comision de los mecanicos
        self.label2.config(text="En cuanto desea disminuir la comisión de los mecanicos?")

        criterios_nuevos = ["Disminución"]
        valores_iniciales_nuevos = ["0"]
        habilitado_nuevos = [True]

        nuevo_frame2 = FieldFrame(self, "Criterio", criterios_nuevos, "Valor", valores_iniciales_nuevos, habilitado_nuevos)

        self.frame2.destroy()
        self.frame2 = nuevo_frame2
        self.frame2.pack(padx=10, pady=10)
        self.idFun = 4.22
    
    def funcionalidad4_2MecanicosFinal(self, valores):
        mecanicosDisminuir = list() 
        disminucion = int(valores[0]) * -1
        
        if admin.ordenMenosRentable == "Reparación de Carros":
            mecanicosDisminuir = admin.obtenerMecanicosAfines("Carro")
        
        elif admin.ordenMenosRentable == "Reparación de Motos":
            mecanicosDisminuir = admin.obtenerMecanicosAfines("Moto")
        
        for i in mecanicosDisminuir: 
            mecanicosDisminuir[i].recibirComision(disminucion)

        self.frame2.destroy()
        self.label2.config(text=f"Le has diminuido la comision a los mecanicos en:\n{valores[0]} unidades")
    

    def funcionalidad4_3(self):
        self.frame2.destroy()
        
        admin.finanzas()
        self.label1.config(text="Este es el resumen general de su taller", font=("Arial", 16))
        
        self.label2.config(text="\n "
                       f"Cartera final: {admin.getInventario().getCartera()}\n "
                       f"Gastos: {admin.getInventario().getGastos()}\n "
                       f"Ingresos: {admin.getInventario().getIngresos()}\n "
                       f"Numero de Ordenes: {admin.numOrdenes()}\n "
                       f"Numero de mecanicos: {len(admin.getMecanicos())}\n "
                       f"Servicio menos rentable: {admin.ordenMasRentable()}\n "
                       f"Servicio mas rentable: {admin.ordenMenosRentable()} \n "
                       f"Calificación del taller: {admin.getCalificacionTaller()}")
        self.idFun = 4.3
        

    def funcionalidad5(self):
        self.label1.config(text="Realizar encuesta", font=("Arial", 16))
        self.label2.config(text="¡Tu opinion nos ayudara a mejorar!")

        criterios_nuevos = ["Nombre", "Mecanico"]
        valores_iniciales_nuevos = [" ", " "]
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
    #serializador(admin)
    VentanaUsuario()
    

    