from src.gestorAplicacion.tallerMecanica.Repuestos import Repuestos

class RepuestosGenericos(Repuestos):

    def __init__(self):
        super().__init__()

    
    def verificarDisponibilidad(self, tiporepuesto, repuestos):
        
        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:
                if repuesto[0] == repuestos and repuesto[1] > 0:
                    return True
                else:
                    return False
        
        elif (tiporepuesto == "Frenos"):
            
            for repuesto in self._repuestosFrenos:

                if repuesto[0] == repuestos and repuesto[1] > 0:
                    return True
                else:
                    return False
        
        elif (tiporepuesto == "Electrico"):

            for repuesto in self._repuestosElectrico:

                if repuesto[0] == repuestos and repuesto[1] > 0:
                    return True
                else:
                    return False
                
        elif (tiporepuesto == "Llantas"):

            for repuesto in self._repuestosLlantas:

                if repuesto[0] == repuestos and repuesto[1] > 0:
                    return True
                else:
                    return False
                
        elif (tiporepuesto == "Carroceria"):
            
            for repuesto in self._repuestosCarroceria:

                if repuesto[0] == repuestos and repuesto[1] > 0:
                    return True
                else:
                    return False

    def repuestosDisponibles(self, tiporepuesto):
        
        repuestosDisponibles = []

        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:
                if  repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
        
        elif (tiporepuesto == "Frenos"):
            
              for repuesto in self._repuestosFrenos:
                if repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
        
        elif (tiporepuesto == "Electrico"):

              for repuesto in self._repuestosElectrico:
                if repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
                
        elif (tiporepuesto == "Llantas"):

             for repuesto in self._repuestosLlantas:
                if repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
                
        elif (tiporepuesto == "Carroceria"):
            
             for repuesto in self._repuestosCarroceria:
                if repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue

        return repuestosDisponibles
    

    def aumentarPrecio(self, aumento, tiporepuesto):
        
        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:

                repuesto[2] += aumento
        
        elif (tiporepuesto == "Frenos"):

            for repuesto in self._repuestosFrenos:

                repuesto[2] += aumento

        elif (tiporepuesto == "Electrico"):

            for repuesto in self._repuestosElectrico:

                repuesto[2] += aumento
        
        elif (tiporepuesto == "Llantas"):

            for repuesto in self._repuestosLlantas:

                repuesto[2] += aumento

        elif (tiporepuesto == "Carroceria"):

            for repuesto in self._repuestosCarroceria:

                repuesto[2] += aumento


    def disminuirPrecio(self, aumento, tiporepuesto):

         if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:

                repuesto[2] -= aumento
        
         elif (tiporepuesto == "Frenos"):

            for repuesto in self._repuestosFrenos:

                repuesto[2] -= aumento

         elif (tiporepuesto == "Electrico"):

            for repuesto in self._repuestosElectrico:

                repuesto[2] -= aumento
        
         elif (tiporepuesto == "Llantas"):

            for repuesto in self._repuestosLlantas:

                repuesto[2] -= aumento

         elif (tiporepuesto == "Carroceria"):

            for repuesto in self._repuestosCarroceria:

                repuesto[2] -= aumento
                

    def obtenerPrecio(self, tiporepuesto, repuestos):
        precio = 0
        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:
                
                if repuesto[0] == repuestos:
                   
                    precio = repuesto[2]
                
        elif (tiporepuesto == "Frenos"):

            for repuesto in self._repuestosFrenos:

                if repuesto[0] == repuestos:

                    precio = repuesto[2]
                
        elif (tiporepuesto == "Electrico"):

            for repuesto in self._repuestosElectrico:

                if repuesto[0] == repuestos:

                    precio = repuesto[2]
        
        elif (tiporepuesto == "Llantas"):

            for repuesto in self._repuestosLlantas:

                if repuesto[0] == repuestos:

                    precio = repuesto[2]
                
        elif (tiporepuesto == "Carroceria"):

            for repuesto in self._repuestosCarroceria:

                if repuesto[0] == repuestos:

                    precio = repuesto[2]
        
        return precio
    
    def obtenerCantidad(self, tiporepuesto, repuestos):

        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:

                if repuesto[0] == repuestos:

                    return repuesto[1]
                
        elif (tiporepuesto == "Frenos"):

            for repuesto in self._repuestosFrenoss:

                if repuesto[0] == repuestos:

                    return repuesto[1]
                
        elif (tiporepuesto == "Electrico"):

            for repuesto in self._repuestosElectrico:

                if repuesto[0] == repuestos:

                    return repuesto[1]
        
        elif (tiporepuesto == "Llantas"):

            for repuesto in self._repuestosLlantas:

                if repuesto[0] == repuestos:

                    return repuesto[1]
                
        elif (tiporepuesto == "Carroceria"):

            for repuesto in self._repuestosCarroceria:

                if repuesto[0] == repuestos:

                    return repuesto[1]
                
        def aumentarCantidad(self, cantidad, tipo, repuesto):

            if (tiporepuesto == "Motor"):

                for repuesto in self._repuestosMotor:

                    if repuesto[0] == repuestos:

                        repuesto[1] += cantidad
                
            elif (tiporepuesto == "Frenos"):

                for repuesto in self._repuestosFrenos:

                     if repuesto[0] == repuestos:

                         repuesto[1] += cantidad
                        
            elif (tiporepuesto == "Electrico"):

                for repuesto in self._repuestosElectrico:

                    if repuesto[0] == repuestos:

                        repuesto[1] += cantidad
                
            elif (tiporepuesto == "Llantas"):

                for repuesto in self._repuestosLlantas:

                    if repuesto[0] == repuestos:

                         repuesto[1] += cantidad
                        
            elif (tiporepuesto == "Carroceria"):

                for repuesto in self._repuestosCarroceria:

                    if repuesto[0] == repuestos:

                         repuesto[1] += cantidad
