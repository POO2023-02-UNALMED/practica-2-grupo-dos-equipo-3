from abc import ABC,abstractclassmethod

class CalificacionMecanico(ABC):
    
    @abstractclassmethod
    def mecanicoSeleccionado(self, seleccion):
        pass
    
    @abstractclassmethod
    def mecanicosActivosCliente(self):
        pass
    
    @abstractclassmethod
    def calificar_mecanico(self, mecanico, calificacion):
        pass
    
    @abstractclassmethod
    def dejarComisionMecanico(self, mecanico, comision):
        pass
    
    @abstractclassmethod
    def premiarPorEncuesta(self, mecanico, administrador):
        pass
    
    @abstractclassmethod
    def calificarTaller(self, admin, calificacion):
        pass