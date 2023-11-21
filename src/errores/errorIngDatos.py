from src.errores.errorApli import ErrorAplicacion

class ErrorIngresoDatos(ErrorAplicacion):
    def __init__(self, err=""):
        super().__init__("Error al ingresar datos: " + err)
        
    def display(self):
        return self.args[0]
