from src.errores.errorIngDatos import ErrorIngresoDatos

class ErrorVehiculoElejido(ErrorIngresoDatos):
    def __init__(self):
        super().__init__("Vehiculo elejido no disponible (Elejir Moto o Carro)")
        
    def display(self):
        return self.args[0]