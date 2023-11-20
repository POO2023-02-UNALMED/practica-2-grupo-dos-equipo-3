from src.gestorAplicacion.errores.ErrorAplicacion import ErrorAplicacion

class ErrorIngresoDatos(ErrorAplicacion):
    def __init__(self):
        super().__init__("Error Ingreso Datos")