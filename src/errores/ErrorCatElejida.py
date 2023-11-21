from src.errores.errorIngDatos import ErrorIngresoDatos

class ErrorCategoriaElejido(ErrorIngresoDatos):
    def __init__(self):
        super().__init__("Categoria elejido no disponible (Elejir Deluxe o Generico)")
        
    def display(self):
        return self.args[0]