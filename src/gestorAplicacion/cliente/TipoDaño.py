from Vehiculo import Vehiculo

class TipoDaño:
    tiposDeDaño = []
    
    def __init__(self, tipo, vehiculo:Vehiculo=None) -> None:
        self._vehiculos = []
        self._tipo = tipo
        TipoDaño.tiposDeDaño.append(self)
        if(Vehiculo != None):
            self._vehiculos.append(Vehiculo)
        
    def getVehiculos(self):
        return self._vehiculos

    def setVehiculos(self, vehiculos):
        self._vehiculos = vehiculos

    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo 
    