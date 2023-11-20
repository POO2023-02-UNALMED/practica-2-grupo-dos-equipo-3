import datetime
from src.gestorAplicacion.cliente.Vehiculo import Vehiculo
from src.gestorAplicacion.tallerMecanica.Administrador import Administrador
from src.gestorAplicacion.tallerMecanica.Mecanicos import Mecanicos

class Orden:
    serialVersionUID = 1
    asignadorId = 1
    numOrdenes = 0
    ordenesTotales = []
 
    def __init__(self,tipo:str,cliente, mecanico:Mecanicos, admin:Administrador, vehiculo:Vehiculo,precio):	
        self._tipo = tipo
        self._cliente = cliente
        self._mecanico = mecanico
        self._admin = admin
        self._id = Orden.asignadorId
        self._estado = False
        self._fecha = datetime()
        self._vehiculo = vehiculo
        self._precio = precio
        Orden.asignadorId += 1
        Orden.numOrdenes += 1
        self._mecanico.getOrdenes().append(self)
        self._admin.getOrdenes().append(self)
        
    def completarOrden(self):
        if self._estado == False:
            self._estado = True
            return "Has completado una orden"
        else:
            return "Ya has completado esta orden"
    
    def getTipo(self):
        return self._tipo

    def setTipo(self,tipo):
        self._tipo = tipo

    def getFecha(self):
        return self._fecha

    def setFecha(self, fecha):
        self._fecha = fecha

    def getCliente(self):
        return self._cliente

    def setCliente(self, cliente):
        self._cliente = cliente

    def getMecanico(self):
        return self._mecanico

    def setMecanico(self, mecanico):
        self._mecanico = mecanico

    def getAdmin(self):
        return self._admin

    def setAdmin(self, admin):
        self._admin = admin


    def isEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    def getId(self):
        return self._id
    
    def setId(self,id):
        self._id = id

    def getRepuesto(self):
        return self._repuesto

    def setRepuesto(self, repuesto):
        self._repuesto = repuesto

    def getPrecio(self):
        return self._precio

    def setPrecio(self,precio):
        self._precio = precio
        
    def getVehiculo(self):
        return self._vehiculo

    def setVehiculo(self, vehiculo):
        self._vehiculo = vehiculo
        
    @classmethod
    def getAsignadorId(cls):
        return cls.asignadorId

    @classmethod
    def setAsignadorId(cls, asignadorId):
        cls.asignadorId = asignadorId

    @classmethod
    def getNumOrdenes(cls):
        return cls.numOrdenes

    @classmethod
    def setNumOrdenes(cls, numOrdenes):
        cls.numOrdenes = numOrdenes

    @classmethod
    def getOrdenesTotales(cls):
        return cls.ordenesTotales

    @classmethod
    def setOrdenesTotales(cls, ordenesTotales):
        cls.ordenesTotales = ordenesTotales
	
    def resumenOrden(self):
        return "Orden: " + self.getTipo() + "\n" + "Fecha: " + self.getFecha() + "\n" + "Cliente: " + self.getCliente().getNombre() + "\n" + "Mecanico: " + self.getMecanico().getNombre() + "\n" + "OrdenId: " + self.getId() + "\n" + "Tipo de daño: " + self.getVehiculo().getTipoDeDanio().getTipo() + "\n" + "Repuesto: " + self.getRepuesto() + "\n" + "Precio: " + self.getPrecio()
    
    def resumenOrdenRepuestos1(self, tipoDañoRepuesto):
        return "Orden: " + self.getTipo() + "\n" + "Fecha: " + self.getFecha() + "\n" + "OrdenId: " + self.getId() + "\n" + "Repuesto usado para: " + tipoDañoRepuesto + "\n" +  "Repuesto: " + self.getRepuesto() + "\n" + "Precio: " + self.getPrecio()
	
    def resumenOrdenRepuestos2(self, tipoDañoRepuesto):
        return "Orden: " + self.getTipo() + "\n" + "Fecha: " + self.getFecha() + "\n" + "OrdenId: " + self.getId() + "\n" + "Repuesto usado para: " + tipoDañoRepuesto + "\n" + "Repuesto: " + self.getRepuesto() + ", " + self.getRepuesto2() + "\n" + "Precio: " + self.getPrecio()
    
    def getTipo_repuesto(self):
        return self._tipo_repuesto

    def setTipo_repuesto(self, tipo_repuesto):
        self._tipo_repuesto = tipo_repuesto

    def getRepuesto2(self):
        return self._repuesto2

    def setRepuesto2(self, repuesto2):
        self._repuesto2 = repuesto2