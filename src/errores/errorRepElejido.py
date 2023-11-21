from src.errores.errorIngDatos import ErrorIngresoDatos

class ErrorRepuestoElejido(ErrorIngresoDatos):
    def __init__(self):
        super().__init__("Repuesto elejido no disponible o escrito incorrectamente")
        
    def display(self):
        return self.args[0]