
class Proveedor:

    def __init__(self, nombre, administrador, id, repuestoDeluxe1,
                 repuestoGenerico1):
        self.nombre = nombre
        self._administrador = administrador
        self._id = id
        self._repuestosDeluxe = repuestoDeluxe1
        self._repuestosGenericos = repuestoGenerico1

    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getAdministrador(self):
        return self._administrador
    def setAdministrador(self, admin):
        self._administrador = admin

    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id

    def getRepuestosDeluxe(self):
        return self._repuestosDeluxe
    def setRepuestosDeluxe(self, repuesto):
        self._repuestosDeluxe = repuesto

    def getRepuestosGenericos(self):
        return self._repuestosGenericos
    def setRepuestosGenericos(self, repuestos):
        self._repuestosGenericos = repuestos

    
        