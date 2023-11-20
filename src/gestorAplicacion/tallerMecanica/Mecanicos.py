from src.gestorAplicacion.tallerMecanica.Administrador import Administrador

class Mecanicos:
    serialVersionUID = 1
    numMecanicos = 0
    
    def __init__(self, nombre, afinidad,administrador:Administrador):
        self._vehiculos = []
        self._clientes = []
        self._ordenes = []
        self._calificaciones = []
        self._ordenesFinalizadas = []
        self._serviciosMax = 5
        self._nombre = nombre
        self._afinidad = afinidad
        self._administrador = administrador
        Mecanicos.numMecanicos += 1
        
    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre

    def getAfinidad(self):
        return self._afinidad

    def setAfinidad(self, afinidad):
        self._afinidad = afinidad
        
    def getVehiculos(self):
        return self._vehiculos

    def setVehiculos(self, vehiculos):
        self._vehiculos = vehiculos

    def getClientes(self):
        return self._clientes

    def setClientes(self, clientes):
        self._clientes = clientes

    def getAdministrador(self):
        return self._administrador

    def setAdministrador(self, administrador):
        self._administrador = administrador

    def getOrdenes(self):
        return self._ordenes

    def setOrdenes(self, ordenes):
        self._ordenes = ordenes

    def getSalario(self):
        return self._salario

    def setSalario(self, salario):
        self._salario = salario
        
    def getComisiones(self):
        return self._comisiones

    def setComisiones(self, comisiones):
        self._comisiones = comisiones

    def getCalificacion(self):
        return self._calificacion

    def setCalificacion(self, calificacion):
        self._calificacion = calificacion

    def getCalificaciones(self):
        return self._calificaciones

    def setCalificaciones(self, calificaciones):
        self._calificaciones = calificaciones
  
    @classmethod
    def getNumMecanicos(cls):
        return cls.numMecanicos

    @classmethod
    def setNumMecanicos(cls,numMecanicos):
        cls.numMecanicos = numMecanicos
	
    def getServiciosMax(self):
        return self._serviciosMax
    
    def setServiciosMax(self, serviciosMax):
        self._serviciosMax = serviciosMax
        
    def consultarOrden(self, id):
        orden = self._ordenes[0]
        for i in range(len(self._ordenes)):
            if (id == self._ordenes[i].getId()):
                orden = self._ordenes[i]
			
        return orden
	
    def recibirComision(self, comision):
        self._comisiones = self._comisiones + comision
        
    def reparar(self, orden, pasos, admin:Administrador):
        claveMotor1 = 15432
        claveMotor2 = 12354
        claveFrenos1 = 13425
        claveFrenos2 = 12354
        claveElectrico1 = 13245
        claveElectrico2 = 45123
        claveCarroceria1 = 14532
        claveCarroceria2 = 12453
        claveLlantas1 = 52431
        claveLlantas2 = 12543
        completado = ""
		
        if(orden.getVehiculo().getTipoDeDanio().getTipo() == "Motor"):
            if (pasos == claveMotor1 or pasos == claveMotor2):
                orden.getVehiculo().setTipoDeDanio(None,admin)
                completado = "Si"
                self._ordenesFinalizadas.append(orden)
					
            else:
                orden.getVehiculo().falloMecanico(admin)
                completado = "No"
		
        elif(orden.getVehiculo().getTipoDeDanio().getTipo() == "Frenos"):
            if (pasos == claveFrenos1 or pasos == claveFrenos2):
                orden.getVehiculo().setTipoDeDanio(None,admin)
                completado = "Si"
                self._ordenesFinalizadas.append(orden)
					
            else:
                orden.getVehiculo().falloMecanico(admin)
                completado = "No"
                
        elif(orden.getVehiculo().getTipoDeDanio().getTipo() == "Electrico"):
            if (pasos == claveElectrico1 or pasos == claveElectrico2):
                orden.getVehiculo().setTipoDeDanio(None,admin)
                completado = "Si"
                self._ordenesFinalizadas.append(orden)
				
            else:
                orden.getVehiculo().falloMecanico(admin)
                completado = "No"
        elif(orden.getVehiculo().getTipoDeDanio().getTipo() == "Llantas"):
            if (pasos == claveLlantas1 or pasos == claveLlantas2):
                orden.getVehiculo().setTipoDeDanio(None,admin)
                completado = "Si"
                self._ordenesFinalizadas.append(orden)
				
		
            else:
                orden.getVehiculo().falloMecanico(admin)
                completado = "No"
    
        elif(orden.getVehiculo().getTipoDeDanio().getTipo() == "Carroceria"):
            if (pasos == claveCarroceria1 or pasos == claveCarroceria2):
                orden.getVehiculo().setTipoDeDanio(None,admin)
                completado = "Si"
                self._ordenesFinalizadas.append(orden)
				
            else:
                self._orden.getVehiculo().falloMecanico(admin)
                completado = "No"
		
        if (completado == "Si"):
            return True
        else:
            return False
        
    def getOrdenesFinalizadas(self):
        return self._ordenesFinalizadas

    def setOrdenesFinalizadas(self, ordenesFinalizadas):
        self._ordenesFinalizadas = ordenesFinalizadas
	
    def añadirCliente(self, cliente):
        self._clientes.append(cliente)