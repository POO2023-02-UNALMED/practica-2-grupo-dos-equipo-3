from Repuestos import Repuestos
class repuestoDeluxe(Repuestos):

    def __init__(self):
        super().__init__(self)

    def verificarDisponibilidad(self, tiporepuesto, repuesto):
        
        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:
                if repuesto[0] == repuesto and repuesto[1] > 0:
                    return True
                else:
                    return False
        
        elif (tiporepuesto == "Frenos"):
            
            for repuesto in self._repuestosFrenos:

                if repuesto[0] == repuesto and repuesto[1] > 0:
                    return True
                else:
                    return False
        
        elif (tiporepuesto == "Electrico"):

            for repuesto in self._repuestosElectrico:

                if repuesto[0] == repuesto and repuesto[1] > 0:
                    return True
                else:
                    return False
                
        elif (tiporepuesto == "Llantas"):

            for repuesto in self._repuestosLlantas:

                if repuesto[0] == repuesto and repuesto[1] > 0:
                    return True
                else:
                    return False
                
        elif (tiporepuesto == "Carroceria"):
            
            for repuesto in self._repuestosCarroceria:

                if repuesto[0] == repuesto and repuesto[1] > 0:
                    return True
                else:
                    return False

    def repuestosDisponibles(self, tiporepuesto):
        
        repuestosDisponibles = []

        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:
                if repuesto[0] == repuesto and repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
        
        elif (tiporepuesto == "Frenos"):
            
              for repuesto in self._repuestosFrenos:
                if repuesto[0] == repuesto and repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
        
        elif (tiporepuesto == "Electrico"):

              for repuesto in self._repuestosElectrico:
                if repuesto[0] == repuesto and repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
                
        elif (tiporepuesto == "Llantas"):

             for repuesto in self._repuestosLlantas:
                if repuesto[0] == repuesto and repuesto[1] > 0:
                    repuestosDisponibles.append(repuesto[0])
                else:
                    continue
                
        elif (tiporepuesto == "Carroceria"):
            
             for repuesto in self._repuestosCarroceria:
                if repuesto[0] == repuesto and repuesto[1] > 0:
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
                

    def obtenerPrecio(self, tiporepuesto, repuesto):

        if (tiporepuesto == "Motor"):

            for repuesto in self._repuestosMotor:

                if repuesto[0] == repuesto and self.verificarDisponibilidad(tiporepuesto, repuesto):

                    return repuesto[2]
                
        elif (tiporepuesto == "Frenos"):

            for repuesto in self._repuestosFrenos:

                if repuesto[0] == repuesto and self.verificarDisponibilidad(tiporepuesto, repuesto):

                    return repuesto[2]
                
        elif (tiporepuesto == "Electrico"):

            for repuesto in self._repuestosElectrico:

                if repuesto[0] == repuesto and self.verificarDisponibilidad(tiporepuesto, repuesto):

                    return repuesto[2]
        
        elif (tiporepuesto == "Llantas"):

            for repuesto in self._repuestosLlantas:

                if repuesto[0] == repuesto and self.verificarDisponibilidad(tiporepuesto, repuesto):

                    return repuesto[2]
                
        elif (tiporepuesto == "Carroceria"):

            for repuesto in self._repuestosCarroceria:

                if repuesto[0] == repuesto and self.verificarDisponibilidad(tiporepuesto, repuesto):

                    return repuesto[2]

        


