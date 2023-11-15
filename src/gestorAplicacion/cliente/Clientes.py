from cliente.Vehiculo import Vehiculo
from tallerMecanica.Administrador import Administrador
from tallerMecanica.Mecanicos import Mecanicos
from tallerMecanica.Orden import Orden
from CalificaciónMecanico import CalificaciónMecanico

class Clientes(CalificaciónMecanico):
    serialVersionUID = 1
    asignadorId = 0
    clientes = []
    
    def __init__(self, nombre, vehiculo):
        self._cartera = 10000000
        self._vehiculos = []
        self._ordenes = []
        
        self._nombre = nombre
        self.vehiculos.append(vehiculo)
        self._id = Clientes.asignadorId
        Clientes.asignadorId += 1
        Clientes.clientes.append(self)
        
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id
        
    def getCartera(self):
        return self._cartera

    def setCartera(self, cartera):
        self._cartera = cartera

    def getVehiculos(self):
        return self._vehiculos

    def setVehiculos(self, vehiculos):
        self._vehiculos = vehiculos

    def getOrdenes(self):
        return self._ordenes

    def setOrdenes(self, ordenes):
        self._ordenes = ordenes
        
    def crearOrden(self, vehiculo:Vehiculo, mecanico:Mecanicos, admin:Administrador, precio):
        orden = None
        if str(vehiculo) == "Carro":
            orden = Orden("Carro", self, mecanico, admin, vehiculo, precio)
            self._ordenes.append(orden)

        if str(vehiculo) == "Moto":
            orden = Orden("Moto", self, mecanico, admin, vehiculo, precio)
            self._ordenes.append(orden)
		
        return orden
	
    def asignarVehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)
        
    @classmethod
    def getAsignadorId(cls):
        return cls.asignadorId

    @classmethod
    def setAsignadorId(cls, asignadorId):
        cls.asignadorId = asignadorId
        
    @classmethod 
    def getClientes(cls):
        return cls.clientes

    @classmethod 
    def setClientes (cls, clientes):
        cls.clientes = clientes
		
    #Encuesta 
    def mecanicoSeleccionado(self, seleccion):
        return self._ordenes[seleccion - 1].getMecanico()

    def mecanicosActivosCliente(self):
        mecanicosCliente = []
        for i in range(len(self.getOrdenes())):
            mecanicosCliente.append(self.getOrdenes()[i].getMecanico())
            
        return  mecanicosCliente
	
    def calificar_mecanico(self, mecanico:Mecanicos, calificacion):
        mecanico.calificaciones.append(calificacion)
        suma_calificaciones = sum(mecanico.calificaciones)
        
        cantidad_calificaciones = len(mecanico.calificaciones)
        promedio = suma_calificaciones // cantidad_calificaciones if cantidad_calificaciones > 0 else 0

        mecanico.setCalificacion(promedio)

    def dejarComisionMecanico(self, mecanico:Mecanicos, comision):
        mecanico.setComisiones(mecanico.getComisiones() + comision)

    def premiarPorEncuesta(self, mecanico:Mecanicos, administrador:Administrador):
        if len(mecanico.getCalificaciones()) >= 3 and mecanico.getCalificacion() >= 4:
            mecanico.setComisiones(mecanico.getComisiones() + 10000)
	
    def pagar(self, precio):
        self._cartera -= precio
        self._ordenes[0].getAdmin().getInventario().recibirDinero(precio)
        
    def calificarTaller(self, admin:Administrador, calificacion):
        admin.getCalificacionesTaller().append(calificacion)
        suma_calificaciones = sum(admin.getCalificacionesTaller())
        cantidad_calificaciones = len(admin.getCalificacionesTaller())

        promedio = suma_calificaciones // cantidad_calificaciones if cantidad_calificaciones > 0 else 0

        admin.setCalificacionTaller(promedio)
