from src.errores.errorCri import ErrorCritico

class ErrorClienteNone(ErrorCritico):

    def __init__(self, err=""):
        super().__init__("El cliente ingresado no existe")
    
    def display(self):
        return self.args[0]
    
class ErrorMecanicoNone(ErrorCritico):

    def __init__(self, err=""):
        super().__init__("El mecanico ingresado no existe")
    
    def display(self):
        return self.args[0]
    
class ErrorNoOrdenes(ErrorCritico):

    def __init__(self, err=""):
        super().__init__("Actualmente no existen ordenes")

    def display(self):
        return self.args[0]
    

