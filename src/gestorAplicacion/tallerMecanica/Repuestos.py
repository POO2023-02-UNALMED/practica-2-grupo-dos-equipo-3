from abc import ABC, abstractmethod

class Repuestos(ABC):

    def __init__(self):
        
        self._repuestosMotor = [['Bujia', 0, 0], ['Filtro de aceite', 0, 0]]
        self._repuestosFrenos = [['Pastilla de frenos', 0, 0], ['Liquido de frenos', 0, 0]]
        self._repuestosElectrico = [['Bateria', 0, 0], ['Focoss', 0, 0]]
        self._repuestosLlantas = [['Valvula', 0, 0], ['Tapa de la valvula', 0, 0]]
        self._repuestosCarroceria = [['Pintura', 0, 0], ['Espejos', 0, 0]]
        self._proveedor = None

    @abstractmethod
    def verificarDisponibilidad(self, tiporepuesto, repuesto):
        pass

    @abstractmethod
    def repuestosDisponibles(self, tiporepuesto):
        pass

    @abstractmethod
    def aumentarPrecio(self, aumento, tiporepuesto):
        pass

    @abstractmethod
    def disminuirPrecio(self, aumento, tiporepuesto):
        pass

    @abstractmethod
    def obtenerPrecio(self, tiporepuesto, tipo):
        pass
        

    def setProveedor(self, proveedor):
        self._proveedor = proveedor
    def getProveedor(self):
        return self._proveedor
        

    def getRepuestosMotor(self):
        return self._repuestosMotor
    def setRepuestosMotor(self, repuestosMotor):
        self._repuestosMotor = repuestosMotor

    def getRepuestosFrenos(self):
        return self._repuestosFrenos
    def setRepuestosFrenos(self, repuestosFrenos):
        self._repuestosFrenos = repuestosFrenos

    def getRepuestosElectrico(self):
        return self._repuestosElectrico
    def setRepuestosElectrico(self, repuestosElectrico):
        self._repuestosElectrico = repuestosElectrico

    def getRepuestosLlantas(self):
        return self._repuestosLlantas
    def setRepuestosLlantas(self, repuestosLlantas):
        self._repuestosLlantas = repuestosLlantas

    def getRepuestosCarroceria(self):
        return self._repuestosCarroceria
    def setRepuestosCarroceria(self, repuestosCarroceria):
        self._repuestosCarroceria = repuestosCarroceria
