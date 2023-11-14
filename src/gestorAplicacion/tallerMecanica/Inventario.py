from Administrador import Administrador
from RepuestosDeluxe import repuestoDeluxe
from RepuestosGenericos import RepuestosGenericos
from PreciosBase import preciosBase

class Inventario():

    def __init__(self, admin, repuestosDeluxe, repuestosGenericos):

        self._admin = admin
        self._repuestosDeluxe = repuestosDeluxe
        self._repuestosGenericos = repuestosGenericos
        self._precioMoto = preciosBase.SERVICIOMOTO.value
        self._precioCarro = preciosBase.SERVICIOCARRO.value
        self._salarioAdmin = preciosBase.SALARIOADMIN.value
        self._salarioMecanico = preciosBase.SALARIOMECANICO.value
        self._cartera = 10000000000
        self._ingresos = 0
        self._gastos = 0

    
    def getAdministrador(self):
        return self._admin
    def setAdministrador(self, admin):
        self._admin = admin
    
    def getRepuestosDeluxe(self):
        return self._repuestosDeluxe
    def setRepuestosDeluxe(self, repuestos):
        self._repuestosDeluxe = repuestos

    def getRepuestoGenericos(self):
        return self._repuestosGenericos
    def setRepuestosGenericos(self, repuestos):
        self._repuestosGenericos = repuestos

    def getPrecioMoto(self):
        return self._precioMoto
    
    def getPrecioCarro(self):
        return self._precioCarro
    
    def getSalarioAdmin(self):
        return self._salarioAdmin
    
    def getSalarioMecanico(self):
        return self._salarioMecanico
    
    def getIngresos(self):
        return self._ingresos
    def setIngresos(self, ingresos):
        self._ingresos = ingresos

    def getGastos(self):
        return self._gastos
    def setGastos(self, gastos):
        self._gastos = gastos
    
    def getCartera(self):
        return self._cartera
    
    def consultarRepuestosDisponibles(self, categoria, tiporepuesto):

        if (categoria == "Deluxe"):
            return self._repuestosDeluxe.repuestosDisponibles(tiporepuesto)
        
        elif(categoria == "Generico"):
            return self._repuestosGenericos.repuestosDisponibles(tiporepuesto)
        

    def recibirDinero(self, dinero):
        self._cartera += dinero
        self._ingresos += dinero
    
    def pagar(self, precio):
        self._cartera -= precio
        self._gastos += precio
    
    


        