from src.errores.errorIngDatos import ErrorIngresoDatos

class ErrorCasillasVacias(ErrorIngresoDatos):
    def __init__(self, err=""):
        super().__init__("Hay algunas casillas vacias")
        
    def display(self):
        return self.args[0]