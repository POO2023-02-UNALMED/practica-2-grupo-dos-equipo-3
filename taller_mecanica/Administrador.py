from Orden import Orden

class Administrador:
    def __init__(self, nombre="", id=0,inventario=None) -> None:
        self._nombre = nombre
        self._id = id
        self._inventario = inventario
        
    def añadirCliente(self, cliente):
        self._cliente = cliente
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getMecanicos(self):
        return self._mecanicos

    def setMecanicos(self, mecanicos):
        self._mecanicos = mecanicos

    def getProveedores(self):
        return self._proveedores

    def setProveedores(self, proveedores):
        self._proveedores = proveedores

    def getInventario(self):
        return self._inventario

    def setInventario(self, inventario):
        self._inventario = inventario

    def getOrdenes(self):
        return self._ordenes

    def setOrdenes(self, ordenes):
        self._ordenes = ordenes
	
    def getMecanicosDisponibles(self):
        return self._mecanicosDisponibles

    def setMecanicosDisponibles(self, mecanicosDisponibles):
        self._mecanicosDisponibles = mecanicosDisponibles

    def añadirMecanico(self, mecanico):
        self._mecanicos.append(mecanico)
	
    def despedir(self, mecanico):
        for i in range(len(self._mecanicos)):
            if mecanico == self._mecanicos.get(i):
                self._mecanicos.remove(i)
	
    def añadirProveedor(self, proveedor):
        self._proveedores.append(proveedor)
	
    def consultarOrden(self, id):
        orden = self._ordenes.get(0)
        for i in range(len(self._ordenes)):
            if id == self._ordenes.get(i).getId():
                orden = self._ordenes.get(i)
        return orden
	
    def asignarMecanico(self, nombre):
        mecanicoElegido = self._mecanicos.get(0)
        for i in range(len(self._mecanicos)):
            if self._mecanicos.get(i).getNombre() == self._nombre:
                mecanicoElegido = self._mecanicos.get(i)
        return mecanicoElegido
	
    def verificarMecanicosDisponibles(self, afinidad):
        mecas = []
        for i in range(len(self._mecanicos)):
            if self._mecanicos.get(i).getServiciosMax() > 0 and self._mecanicos.get(i).getAfinidad() == afinidad:
                mecas.append(self.mecanicos.get(i))
        return mecas
	
    def mecanicosTrabajando(self):
        mecanicosTrabajando = []
        for i in range(len(self._mecanicos)):
            if self._mecanicos.get(i).getOrdenes().isEmpty() != True:
                mecanicosTrabajando.append(self._mecanicos.get(i))

        return mecanicosTrabajando
	
    def darComision(self, nombre):
        for i in range(len(self._mecanicosDisponibles)):
            if (self._mecanicosDisponibles.get(i).getNombre() == nombre and self._mecanicosDisponibles.get(i).getAfinidad() == "Moto"):
                self._mecanicosDisponibles.get(i).recibirComision(10000)
            elif (self._mecanicosDisponibles.get(i).getNombre() == nombre and self._mecanicosDisponibles.get(i).getAfinidad() == "Carro"):
                self._mecanicosDisponibles.get(i).recibirComision(8000)

    def generarResumenMasIngresosOpcion1(self, ordenMasRentable:Orden, aumento:int):
        ordenMasRentable.setPrecio(ordenMasRentable.getPrecio() + aumento)
	
    def generarResumenMasIngresosOpcion2Deluxe(self, ordenMasRentable:Orden, aumento:int, tipoRepuesto:str):
        repuestoDeluxe = ordenMasRentable.getAdmin().getInventario().getRepuestosDeluxe()
        repuestoDeluxe.aumentarPrecio(aumento, tipoRepuesto)
	
    def generarResumenMasIngresosOpcion2Generico(self, ordenMasRentable:Orden, aumento, tipoRepuesto):
        repuestoGenerico = ordenMasRentable.getAdmin().getInventario().getRepuestosGenericos()
        repuestoGenerico.aumentarPrecio(aumento, tipoRepuesto)

    def generarResumenMasIngresosOpcion3(self, ordenMasRentable:Orden, aumento):
        mecanico = ordenMasRentable.getMecanico()
        mecanico.setComisiones(mecanico.getComisiones()+ aumento)
	
    def generarResumenMenosIngresosOpcion1(self, ordenMenosRentable:Orden, desaumento):
        if desaumento <= ordenMenosRentable.getPrecio():
            ordenMenosRentable.setPrecio(ordenMenosRentable.getPrecio() - desaumento)
	
    def generarResumenMenosIngresosOpcion2Deluxe(self,ordenMenosRentable:Orden, desaumento, tipoRepuesto):
        repuestoDeluxe = ordenMenosRentable.getAdmin().getInventario().getRepuestosDeluxe()
        repuestoDeluxe.disminuirPrecio(desaumento, tipoRepuesto)
	
    def generarResumenMenosIngresosOpcion2Generico(self, ordenMasRentable:Orden, desaumento, tipoRepuesto):
        repuestoGenerico = ordenMasRentable.getAdmin().getInventario().getRepuestosGenericos()
        repuestoGenerico.disminuirPrecio(desaumento, tipoRepuesto)
	
    def generarResumenMenosIngresosOpcion3(self, ordenMasRentable:Orden, desaumento):
        mecanico = ordenMasRentable.getMecanico()
        if desaumento <= mecanico.getComisiones():
            mecanico.setComisiones(mecanico.getComisiones() - desaumento)

    def resumenGeneral(self):
        sumaSalarios = 0
        for mecanico in self._mecanicosDisponibles:
            sumaSalarios += mecanico.getSalario()
	    
        gastos = sumaSalarios + self._inventario.getGastos()
        ganancia = self._inventario.getIngresos() - gastos
  
        return ganancia

    def ordenMasRentable(self):
        tipo = ""
        gananciasCarro = 0
        gananciasMoto = 0
		
        for i in range(len(self._ordenes)):
            if self._ordenes.get(i).getTipo() == "Carro":
                gananciasCarro = gananciasCarro + self._ordenes.get(i).getPrecio()
            elif self._ordenes.get(i).getTipo() == "Moto":
                gananciasMoto = gananciasMoto + self._ordenes.get(i).getPrecio()

        if gananciasCarro > gananciasMoto:
            tipo = "Reparación de Carros"
        elif gananciasCarro < gananciasMoto:
            tipo = "Reparación de Motos"
        return tipo
	
    def ordenMenosRentable(self):
        tipo = ""
        gananciasCarro = 0
        gananciasMoto = 0
		
        for i in range(len(self._ordenes)):
            if self._ordenes.get(i).getTipo() == "Carro":
                gananciasCarro = gananciasCarro + self._ordenes.get(i).getPrecio()
            elif self._ordenes.get(i).getTipo() == "Moto":
                gananciasMoto = gananciasMoto + self._ordenes.get(i).getPrecio()
		
        if gananciasCarro > gananciasMoto:
            tipo = "Reparación de Motos"
        elif gananciasCarro < gananciasMoto:
            tipo = "Reparación de Carros"
        return tipo
	
    def solicitarRepuestos(self, categoria, tipo, repuesto, cantidad, proveedor_nombre):
        proveedor = None
        for i in range(len(self.getProveedores())):
            if proveedor_nombre == self.getProveedores().get(i).getNombre():
                proveedor = self.getProveedores().get(i)
		
        if categoria == "Deluxe":
            if tipo == "Motor":
                valor = self.getInventario().getRepuestosDeluxe().getRepuestosMotor().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosMotor[repuesto] = valor
    
                valor2 = proveedor.getRepuestosDeluxe().getRepuestosMotor().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosMotor[repuesto] = valor2
			
            elif tipo == "Frenos":
                valor = self.getInventario().getRepuestosDeluxe().getRepuestosFrenos().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosFrenos[repuesto] = valor
				
                valor2 = proveedor.getRepuestosDeluxe().getRepuestosFrenos().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosFrenos[repuesto] = valor2
			
            elif tipo == "Electrico":
                valor = self.getInventario().getRepuestosDeluxe().getRepuestosElectrico().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosElectrico[repuesto] = valor
			
                valor2 = proveedor.getRepuestosDeluxe().getRepuestosElectrico().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosElectrico[repuesto] = valor2	
    		
            elif tipo == "Llantas":
                valor = self.getInventario().getRepuestosDeluxe().getRepuestosLlantas().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosLlantas[repuesto] = valor
				
                valor2 = proveedor.getRepuestosDeluxe().getRepuestosLlantas().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosLlantas[repuesto] = valor2
			
            elif tipo == "Carroceria":
                valor = self.getInventario().getRepuestosDeluxe().getRepuestosCarroceria().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosCarroceria[repuesto] = valor
				
                valor2 = proveedor.getRepuestosDeluxe().getRepuestosCarroceria().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosCarroceria[repuesto] = valor2
		
        elif categoria == "Generico":
            if tipo == "Motor":
                valor = self.getInventario().getRepuestosGenericos().getRepuestosMotor().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosGenericos().repuestosMotor[repuesto] = valor
					
                valor2 = proveedor.getRepuestoGenerico().getRepuestosMotor().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestoGenerico().repuestosMotor[repuesto] = valor2
			
            elif tipo== "Frenos":
                valor = self.getInventario().getRepuestosGenericos().getRepuestosFrenos().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosGenericos().repuestosFrenos[repuesto] = valor
				
                valor2 = proveedor.getRepuestoGenerico().getRepuestosFrenos().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestoGenerico().repuestosFrenos[repuesto] = valor2

            elif tipo== "Electrico":
                valor = self.getInventario().getRepuestosGenericos().getRepuestosElectrico().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosGenericos().repuestosElectrico[repuesto] = valor
			
                valor2 = proveedor.getRepuestoGenerico().getRepuestosElectrico().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestoGenerico().repuestosElectrico[repuesto] = valor2

            elif tipo== "Llantas":
                valor = self.getInventario().getRepuestosGenericos().getRepuestosLlantas().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosGenericos().repuestosLlantas[repuesto] = valor
				
                valor2 = proveedor.getRepuestoGenerico().getRepuestosLlantas().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestoGenerico().repuestosLlantas[repuesto] = valor2
			
			
            elif tipo == "Carroceria":
                valor = self.getInventario().getRepuestosGenericos().getRepuestosCarroceria().get(repuesto)
                valor += cantidad
                self.getInventario().getRepuestosGenericos().repuestosCarroceria[repuesto] = valor
				
                valor2 = proveedor.getRepuestoGenerico().getRepuestosCarroceria().get(repuesto)
                valor2 -= cantidad
                proveedor.getRepuestoGenerico().repuestosCarroceria[repuesto] = valor2
	
    def solicitarRepuestos(self, categoria, tipo, repuesto,repuesto2, cantidad, proveedor_nombre):
        proveedor = None
        for i in range(len(self.getProveedores())):
            if proveedor_nombre == self.getProveedores().get(i).getNombre():
                proveedor = self.getProveedores().get(i)

        if categoria == "Deluxe":
            if tipo == "Motor":
                valor1 = self.getInventario().getRepuestosDeluxe().getRepuestosMotor().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosMotor[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosDeluxe().getRepuestosMotor().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosMotor[repuesto2] = valor2
                
                valor3 = proveedor.getRepuestosDeluxe().getRepuestosMotor().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosMotor[repuesto] = valor3
                valor4 = proveedor.getRepuestosDeluxe().getRepuestosMotor().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosMotor[repuesto2] = valor4
			
            elif tipo == "Frenos":
                valor1 = self.getInventario().getRepuestosDeluxe().getRepuestosFrenos().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosFrenos[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosDeluxe().getRepuestosFrenos().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosFrenos[repuesto2] = valor2
				
                valor3 = proveedor.getRepuestosDeluxe().getRepuestosFrenos().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosFrenos[repuesto] = valor3
                valor4 = proveedor.getRepuestosDeluxe().getRepuestosFrenos().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosFrenos[repuesto2] = valor4
    
            elif tipo == "Electrico":
                valor1 = self.getInventario().getRepuestosDeluxe().getRepuestosElectrico().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosElectrico[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosDeluxe().getRepuestosElectrico().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosElectrico[repuesto2] = valor2
			
                valor3 = proveedor.getRepuestosDeluxe().getRepuestosElectrico().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosElectrico[repuesto] = valor3
                valor4 = proveedor.getRepuestosDeluxe().getRepuestosElectrico().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosElectrico[repuesto2] = valor4
				
            elif tipo == "Llantas":
                valor1 = self.getInventario().getRepuestosDeluxe().getRepuestosLlantas().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosLlantas[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosDeluxe().getRepuestosLlantas().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosLlantas[repuesto] = valor2
				
                valor3 = proveedor.getRepuestosDeluxe().getRepuestosLlantas().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosLlantas[repuesto] = valor3
                valor4 = proveedor.getRepuestosDeluxe().getRepuestosLlantas().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosLlantas[repuesto2] = valor4
			
            elif tipo == "Carroceria":
                valor1 = self.getInventario().getRepuestosDeluxe().getRepuestosCarroceria().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosCarroceria[repuesto,] = valor1
                valor2 = self.getInventario().getRepuestosDeluxe().getRepuestosCarroceria().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosDeluxe().repuestosCarroceria[repuesto2] = valor2
				
                valor3 = proveedor.getRepuestosDeluxe().getRepuestosCarroceria().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosCarroceria[repuesto] = valor3
                valor4 = proveedor.getRepuestosDeluxe().getRepuestosCarroceria().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestosDeluxe().repuestosCarroceria[repuesto2] = valor4

        elif categoria == "Generico":
            if tipo == "Motor":
                valor1 = self.getInventario().getRepuestosGenericos().getRepuestosMotor().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosMotor[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosGenericos().getRepuestosMotor().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosMotor[repuesto2] = valor2
					
                valor3 = proveedor.getRepuestoGenerico().getRepuestosMotor().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestoGenerico().repuestosMotor[repuesto] = valor3
                valor4 = proveedor.getRepuestoGenerico().getRepuestosMotor().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestoGenerico().repuestosMotor[repuesto2] = valor4
			
            elif tipo == "Frenos":
                valor1 = self.getInventario().getRepuestosGenericos().getRepuestosFrenos().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosFrenos[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosGenericos().getRepuestosFrenos().get(repuesto2)
                valor2 = valor2 + cantidad
                self.getInventario().getRepuestosGenericos().repuestosFrenos[repuesto2] = valor2
                valor3 = proveedor.getRepuestoGenerico().getRepuestosFrenos().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestoGenerico().repuestosFrenos[repuesto] = valor3
                valor4 = proveedor.getRepuestoGenerico().getRepuestosFrenos().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestoGenerico().repuestosFrenos[repuesto2] = valor4
			
            elif tipo == "Electrico":
                valor1 = self.getInventario().getRepuestosGenericos().getRepuestosElectrico().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosElectrico[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosGenericos().getRepuestosElectrico().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosElectrico[repuesto2] = valor2
			
                valor3 = proveedor.getRepuestoGenerico().getRepuestosElectrico().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestoGenerico().repuestosElectrico[repuesto] = valor3
                valor4 = proveedor.getRepuestoGenerico().getRepuestosElectrico().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestoGenerico().repuestosElectrico[repuesto2] = valor4

            elif tipo == "Llantas":
                valor1 = self.getInventario().getRepuestosGenericos().getRepuestosLlantas().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosLlantas[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosGenericos().getRepuestosLlantas().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosLlantas[repuesto2] = valor2
				
                valor3 = proveedor.getRepuestoGenerico().getRepuestosLlantas().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestoGenerico().repuestosLlantas[repuesto] = valor3
                valor4 = proveedor.getRepuestoGenerico().getRepuestosLlantas().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestoGenerico().repuestosLlantas[repuesto2] = valor4
		
            elif tipo == "Carroceria":
                valor1 = self.getInventario().getRepuestosGenericos().getRepuestosCarroceria().get(repuesto)
                valor1 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosCarroceria[repuesto] = valor1
                valor2 = self.getInventario().getRepuestosGenericos().getRepuestosCarroceria().get(repuesto2)
                valor2 += cantidad
                self.getInventario().getRepuestosGenericos().repuestosCarroceria[repuesto2] = valor2
                valor3 = proveedor.getRepuestoGenerico().getRepuestosCarroceria().get(repuesto)
                valor3 -= cantidad
                proveedor.getRepuestoGenerico().repuestosCarroceria[repuesto] = valor3
                valor4 = proveedor.getRepuestoGenerico().getRepuestosCarroceria().get(repuesto2)
                valor4 -= cantidad
                proveedor.getRepuestoGenerico().repuestosCarroceria[repuesto2] = valor4

    def proveedoresDisponiblesRepuestosDeluxe(self, tipo):
        proveedoresDisponibles = []
        if (tipo == "Motor"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadMotor("Bujia") and self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadMotor("Filtro de aceite")):
                    proveedoresDisponibles.append(self._proveedores.get(i))
				
        elif (tipo == "Frenos"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadFrenos("Pastilla de frenos") and self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadFrenos("Liquido de frenos")):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        elif (tipo == "Electrico"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadElectrico("Bateria") and self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadElectrico("Focos")):
                    proveedoresDisponibles.append(self._proveedores.get(i))

        elif (tipo == "Llantas"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadLlantas("Valvula") and self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadLlantas("Tapa de la valvula")):
                    proveedoresDisponibles.append(self._proveedores.get(i))

        elif (tipo == "Carroceria"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadCarroceria("Pintura") and self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadCarroceria("Espejos")):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        return proveedoresDisponibles
	
    def proveedoresDisponiblesRepuestosDeluxe(self, tipo, clave):
        proveedoresDisponibles = []
        if (tipo == "Motor"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadMotor(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
				
        elif (tipo == "Frenos"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadFrenos(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        elif (tipo == "Electrico"):	
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadElectrico(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i));
		
        elif (tipo == "Llantas"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadLlantas(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i));
		
        elif (tipo == "Carroceria"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestosDeluxe().verificarDisponibilidadCarroceria(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
                    
        return proveedoresDisponibles
	
    def obtenerMecanicosAfines(self, afinidad):
        mecanicos = []
        for i in range(len(self._mecanicosDisponibles)):
            if(self._mecanicosDisponibles.get(i).getAfinidad() == afinidad):
                mecanicos.append(self._mecanicos.get(i))

        return mecanicos
	
    def proveedoresDisponiblesRepuestosGenerico(self, tipo):
        proveedoresDisponibles = []
        if (tipo == "Motor"):
            for i in range(len(self._proveedores)): 
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadMotor("Bujia") and self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadMotor("Filtro de aceite")):
                    proveedoresDisponibles.append(self._proveedores.get(i))

        elif (tipo == "Frenos"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadFrenos("Pastilla de frenos") and self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadFrenos("Liquido de frenos")):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        elif (tipo == "Electrico"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadElectrico("Bateria") and self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadElectrico("Focos")):
                    proveedoresDisponibles.append(self._proveedores.get(i))

        elif (tipo == "Llantas"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadLlantas("Valvula") and self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadLlantas("Tapa de la valvula")):
                    proveedoresDisponibles.append(self._proveedores.get(i))

        elif (tipo == "Carroceria"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadCarroceria("Pintura") and self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadCarroceria("Espejos")):
                    proveedoresDisponibles.append(self._proveedores.get(i))

        return proveedoresDisponibles
	
    def proveedoresDisponiblesRepuestosGenerico(self, tipo, clave):
        proveedoresDisponibles = []
        if (tipo == "Motor"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadMotor(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        elif (tipo == "Frenos"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadFrenos(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        elif (tipo == "Electrico"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadElectrico(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        elif (tipo == "Llantas"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadLlantas(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        elif (tipo == "Carroceria"):
            for i in range(len(self._proveedores)):
                if (self._proveedores.get(i).getRepuestoGenerico().verificarDisponibilidadCarroceria(clave)):
                    proveedoresDisponibles.append(self._proveedores.get(i))
		
        return proveedoresDisponibles
	
    def finanzas(self):
        for i in range(len(self._mecanicos)):
            self.getInventario().pagar(self.getInventario().getSalarioMecanico().getValor())
            for e in range(len(self._mecanicos.get(i).getOrdenes())):
                if self._mecanicos.get(i).getOrdenes().get(e).getTipo() == "Carro":
                    self.getInventario().recibirDinero(self._mecanicos.get(i).getOrdenes().get(e).getPrecio())
                elif self._mecanicos.get(i).getOrdenes().get(e).getTipo() == "Moto":
                    self.getInventario().recibirDinero(self._mecanicos.get(i).getOrdenes().get(e).getPrecio())
		
        self.getInventario().pagar(self.getInventario().getSalarioAdmin().getValor())
	
    def numOrdenes(self):
        return len(self.getOrdenes())
		
    def getClientes(self):
        return self._clientes
		
    def getClienteNombre(self, nombre):
        cliente = None
        for i in range(len(self.getClientes())):
            if self.getClientes().get(i).getNombre() == nombre:
                cliente = self.getClientes().get(i)
        return cliente

    def getCalificacionTaller(self):
        return self._calificacionTaller

    def setCalificacionTaller(self, calificacionTaller):
        self._calificacionTaller = calificacionTaller

    def getCalificacionesTaller(self):
        return self._calificacionesTaller

    def setCalificacionesTaller(self, calificacionesTaller):
        self._calificacionesTaller = calificacionesTaller

    def getTiposDaño(self):
        return self._tiposDaño

    def setTiposDaño(self, tiposDaño):
        self._tiposDaño = tiposDaño

    def añadirTipoDaño(self, tipo):
        self._tiposDaño.append(tipo)