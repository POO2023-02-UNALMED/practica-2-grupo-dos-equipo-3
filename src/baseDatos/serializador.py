import pickle

from src.gestorAplicacion.cliente import *

from src.gestorAplicacion.tallerMecanica.Administrador import Administrador
from src.gestorAplicacion.tallerMecanica.Mecanicos import Mecanicos
from src.gestorAplicacion.tallerMecanica.Proveedor import Proveedor
from src.gestorAplicacion.tallerMecanica.RepuestosGenericos import RepuestosGenericos
from src.gestorAplicacion.tallerMecanica.RepuestosDeluxe import RepuestosDeluxe
from src.gestorAplicacion.tallerMecanica.Inventario import Inventario

admin = Administrador()

mecanico1 = Mecanicos("Jeronimo", "Carro", admin)
mecanico2 = Mecanicos("Juan", "Moto", admin)
mecanico3 = Mecanicos("Manuela", "Carro", admin)
mecanico4 = Mecanicos("Angelika", "Moto", admin)
mecanico5 = Mecanicos("Fernando Miguel", "Carro", admin)
mecanicos = [mecanico1,mecanico2,mecanico3,mecanico4,mecanico5]

repuestoGenerico1 = RepuestosGenericos()
repuestoGenerico1.setRepuestosMotor([['Bujia', 0, 0], ['Filtro de aceite', 0, 0]]) 
repuestoGenerico1.setRepuestosFrenos([['Pastilla de frenos', 0, 0], ['Liquido de frenos', 0, 0]]) 
repuestoGenerico1.setRepuestosElectrico([['Bateria', 0, 0], ['Focoss', 0, 0]])
repuestoGenerico1.setRepuestosLlantas([['Valvula', 0, 0], ['Tapa de la valvula', 0, 0]])
repuestoGenerico1.setRepuestosCarroceria([['Pintura', 0, 0], ['Espejos', 0, 0]])

repuestoDeluxe1 = RepuestosDeluxe()
repuestoDeluxe1.setRepuestosMotor([['Bujia', 0, 0], ['Filtro de aceite', 0, 0]]) 
repuestoDeluxe1.setRepuestosFrenos([['Pastilla de frenos', 0, 0], ['Liquido de frenos', 0, 0]]) 
repuestoDeluxe1.setRepuestosElectrico([['Bateria', 0, 0], ['Focoss', 0, 0]])
repuestoDeluxe1.setRepuestosLlantas([['Valvula', 0, 0], ['Tapa de la valvula', 0, 0]])
repuestoDeluxe1.setRepuestosCarroceria([['Pintura', 0, 0], ['Espejos', 0, 0]])

proveedor1 = Proveedor("Stuar Little", admin, 123, repuestoDeluxe1, repuestoGenerico1)
repuestoDeluxe1.setProveedor(proveedor1)
repuestoGenerico1.setProveedor(proveedor1)

repuestoGenerico2 = RepuestosGenericos()
repuestoGenerico2.setRepuestosMotor([['Bujia', 0, 0], ['Filtro de aceite', 0, 0]]) 
repuestoGenerico2.setRepuestosFrenos([['Pastilla de frenos', 0, 0], ['Liquido de frenos', 0, 0]]) 
repuestoGenerico2.setRepuestosElectrico([['Bateria', 0, 0], ['Focoss', 0, 0]])
repuestoGenerico2.setRepuestosLlantas([['Valvula', 0, 0], ['Tapa de la valvula', 0, 0]])
repuestoGenerico2.setRepuestosCarroceria([['Pintura', 0, 0], ['Espejos', 0, 0]])

repuestoDeluxe2 = RepuestosDeluxe()
repuestoDeluxe2.setRepuestosMotor([['Bujia', 0, 0], ['Filtro de aceite', 0, 0]]) 
repuestoDeluxe2.setRepuestosFrenos([['Pastilla de frenos', 0, 0], ['Liquido de frenos', 0, 0]]) 
repuestoDeluxe2.setRepuestosElectrico([['Bateria', 0, 0], ['Focoss', 0, 0]])
repuestoDeluxe2.setRepuestosLlantas([['Valvula', 0, 0], ['Tapa de la valvula', 0, 0]])
repuestoDeluxe2.setRepuestosCarroceria([['Pintura', 0, 0], ['Espejos', 0, 0]])

proveedor2 = Proveedor("Bad Bunny", admin, 321, repuestoDeluxe2, repuestoGenerico2)
repuestoDeluxe1.setProveedor(proveedor2)
repuestoGenerico1.setProveedor(proveedor2)

deluxeInventario = RepuestosDeluxe()
deluxeInventario.setRepuestosMotor([['Bujia', 0, 0], ['Filtro de aceite', 0, 0]]) 
deluxeInventario.setRepuestosFrenos([['Pastilla de frenos', 0, 0], ['Liquido de frenos', 0, 0]]) 
deluxeInventario.setRepuestosElectrico([['Bateria', 0, 0], ['Focoss', 0, 0]])
deluxeInventario.setRepuestosLlantas([['Valvula', 0, 0], ['Tapa de la valvula', 0, 0]])
deluxeInventario.setRepuestosCarroceria([['Pintura', 0, 0], ['Espejos', 0, 0]])

genericoInventario = RepuestosGenericos()
genericoInventario.setRepuestosMotor([['Bujia', 0, 0], ['Filtro de aceite', 0, 0]]) 
genericoInventario.setRepuestosFrenos([['Pastilla de frenos', 0, 0], ['Liquido de frenos', 0, 0]]) 
genericoInventario.setRepuestosElectrico([['Bateria', 0, 0], ['Focoss', 0, 0]])
genericoInventario.setRepuestosLlantas([['Valvula', 0, 0], ['Tapa de la valvula', 0, 0]])
genericoInventario.setRepuestosCarroceria([['Pintura', 0, 0], ['Espejos', 0, 0]])

inventario = Inventario(admin, deluxeInventario ,genericoInventario)







