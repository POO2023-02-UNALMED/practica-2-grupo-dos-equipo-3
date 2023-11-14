import random
from taller_mecanica.Administrador import Administrador

class Vehiculo:
    serialVersionUID = 1
    placas = set()
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def __init__(self, tipo, dueno):
        self._tipo = tipo
        self._dueno = dueno
        self._placa = self.generar_placa()

    @classmethod
    def generar_placa(cls):
        placaGenerada = ""
        if placaGenerada not in cls.placas:
            for _ in range(7):
                indice = random.choice(range(len(cls.caracteres)))
                caracter = cls.caracteres[indice]
                placaGenerada += caracter
    
        cls.placas.add(str(placaGenerada))
        return str(placaGenerada)

    def getPlaca(self):
        return self._placa 
    
    def setPlaca(self, placa):
        self._placa = placa 
        
    def getTipoDeDanio(self):
        return self._tipoDeDanio
    
    def setTipoDeDanio(self, tipo, admin:Administrador):
        Tipo = admin.getTiposDaño()[0]
        if tipo == "":
            self._tipoDeDanio = None
        else:
            for i in range(len(admin.getTiposDaño())):
                if admin.getTiposDaño()[i].getTipo() == tipo:
                    Tipo = admin.getTiposDaño()[i]
            self._tipoDeDanio = Tipo

    def getDueno(self):
        return self._dueno

    def setDueno(self, dueno):
        self._dueno = dueno

    def setTipo(self, tipo):
        self._tipo = tipo
        
    def getTipo(self):
        return self._tipo
    
    def falloMecanico(self, admin):
        numeroAleatorio = random.choice(5)
        self._tipoDeDanio = admin.getTiposDaño()[numeroAleatorio]
    
    #Sobrecarga de metodos- aplicar
    def setTipoDeDanio(self, tipoDeDanio):
        self._tipoDeDanio = tipoDeDanio

    def __str__(self):
    	return self.getTipo()