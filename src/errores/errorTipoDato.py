from src.errores.errorIngDatos import ErrorIngresoDatos

class ErrorDato(ErrorIngresoDatos):

    def __init__(self, err=""):
        super().__init__("El dato que ingresaste no es valido")

    def display(self):
        return self.args[0]