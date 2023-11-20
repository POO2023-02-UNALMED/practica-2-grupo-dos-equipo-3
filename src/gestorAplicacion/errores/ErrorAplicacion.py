class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        
        self._mensaje = mensaje
        
    def mostrarMensaje(self):
        return "Error aplicacion: " + self._mensaje