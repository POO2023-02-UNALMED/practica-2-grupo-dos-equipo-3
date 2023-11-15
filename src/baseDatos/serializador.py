import pickle

from gestorAplicacion.cliente.TipoDaño import TipoDaño

from gestorAplicacion.tallerMecanica.Administrador import Administrador
from gestorAplicacion.tallerMecanica.Mecanicos import Mecanicos
from gestorAplicacion.tallerMecanica.Proveedor import Proveedor
from gestorAplicacion.tallerMecanica.RepuestosGenericos import RepuestosGenericos
from gestorAplicacion.tallerMecanica.RepuestosDeluxe import RepuestosDeluxe
from gestorAplicacion.tallerMecanica.Inventario import Inventario

admin = Administrador()

mecanico1 = Mecanicos("Jeronimo", "Carro", admin)
mecanico2 = Mecanicos("Juan", "Moto", admin)
mecanico3 = Mecanicos("Manuela", "Carro", admin)
mecanico4 = Mecanicos("Angelika", "Moto", admin)
mecanico5 = Mecanicos("Fernando Miguel", "Carro", admin)
mecanicos = [mecanico1,mecanico2,mecanico3,mecanico4,mecanico5]

repuestoGenerico1 = RepuestosGenericos()
repuestoGenerico1.setRepuestosMotor([['Bujia', 2, 3000], ['Filtro de aceite', 2, 2010]]) 
repuestoGenerico1.setRepuestosFrenos([['Pastilla de frenos', 2, 1990], ['Liquido de frenos', 2, 2030]]) 
repuestoGenerico1.setRepuestosElectrico([['Bateria', 2, 4567], ['Focoss', 2, 2230]])
repuestoGenerico1.setRepuestosLlantas([['Valvula', 2, 1234], ['Tapa de la valvula', 2, 6872]])
repuestoGenerico1.setRepuestosCarroceria([['Pintura', 2, 4103], ['Espejos', 2, 7891]])

repuestoDeluxe1 = RepuestosDeluxe()
repuestoDeluxe1.setRepuestosMotor([['Bujia', 2, 4050], ['Filtro de aceite', 2, 3110]]) 
repuestoDeluxe1.setRepuestosFrenos([['Pastilla de frenos', 2, 3900], ['Liquido de frenos', 2, 2990]]) 
repuestoDeluxe1.setRepuestosElectrico([['Bateria', 2, 5600], ['Focoss', 2, 4220]])
repuestoDeluxe1.setRepuestosLlantas([['Valvula', 2, 4203], ['Tapa de la valvula', 2, 8980]])
repuestoDeluxe1.setRepuestosCarroceria([['Pintura', 2, 5600], ['Espejos', 2, 9870]])

proveedor1 = Proveedor("Stuar Little", admin, 123, repuestoDeluxe1, repuestoGenerico1)
repuestoDeluxe1.setProveedor(proveedor1)
repuestoGenerico1.setProveedor(proveedor1)

repuestoGenerico2 = RepuestosGenericos()
repuestoGenerico2.setRepuestosMotor([['Bujia', 2, 3450], ['Filtro de aceite', 2, 5600]]) 
repuestoGenerico2.setRepuestosFrenos([['Pastilla de frenos', 3402, 0], ['Liquido de frenos', 2, 6200]]) 
repuestoGenerico2.setRepuestosElectrico([['Bateria', 2, 1203], ['Focoss', 2, 2304]])
repuestoGenerico2.setRepuestosLlantas([['Valvula', 2, 5870], ['Tapa de la valvula', 2, 5060]])
repuestoGenerico2.setRepuestosCarroceria([['Pintura', 2, 2035], ['Espejos', 2, 6093]])

repuestoDeluxe2 = RepuestosDeluxe()
repuestoDeluxe2.setRepuestosMotor([['Bujia', 2, 4205], ['Filtro de aceite', 2, 7600]]) 
repuestoDeluxe2.setRepuestosFrenos([['Pastilla de frenos', 2, 5406], ['Liquido de frenos', 2, 8980]]) 
repuestoDeluxe2.setRepuestosElectrico([['Bateria', 2, 2400], ['Focoss', 2, 4950]])
repuestoDeluxe2.setRepuestosLlantas([['Valvula', 2, 7899], ['Tapa de la valvula', 2, 0]])
repuestoDeluxe2.setRepuestosCarroceria([['Pintura', 2, 3053], ['Espejos', 2, 8999]])

proveedor2 = Proveedor("Bad Bunny", admin, 321, repuestoDeluxe2, repuestoGenerico2)
repuestoDeluxe1.setProveedor(proveedor2)
repuestoGenerico1.setProveedor(proveedor2)

proveedores = [proveedor1, proveedor2]

deluxeInventario = RepuestosDeluxe()
deluxeInventario.setRepuestosMotor([['Bujia', 2, 5060], ['Filtro de aceite', 2, 7080]]) 
deluxeInventario.setRepuestosFrenos([['Pastilla de frenos', 2, 8880], ['Liquido de frenos', 2, 6700]]) 
deluxeInventario.setRepuestosElectrico([['Bateria', 2, 11230], ['Focoss', 2, 9394]])
deluxeInventario.setRepuestosLlantas([['Valvula', 2, 5031], ['Tapa de la valvula', 2, 7893]])
deluxeInventario.setRepuestosCarroceria([['Pintura', 2, 6707], ['Espejos', 2, 9877]])

genericoInventario = RepuestosGenericos()
genericoInventario.setRepuestosMotor([['Bujia', 2, 4506], ['Filtro de aceite', 2, 6705]]) 
genericoInventario.setRepuestosFrenos([['Pastilla de frenos', 2, 6089], ['Liquido de frenos', 2, 5980]]) 
genericoInventario.setRepuestosElectrico([['Bateria', 2, 8999], ['Focoss', 2, 8971]])
genericoInventario.setRepuestosLlantas([['Valvula', 2, 4560], ['Tapa de la valvula', 2, 5697]])
genericoInventario.setRepuestosCarroceria([['Pintura', 2, 5697], ['Espejos', 2, 7812]])

inventario = Inventario(admin, deluxeInventario ,genericoInventario)

motor = TipoDaño("Motor")
frenos = TipoDaño("Frenos")
electrico = TipoDaño("Electrico")
llantas = TipoDaño("Llantas")
carroceria = TipoDaño("Carroceria")

admin.añadirTipoDaño(motor)
admin.añadirTipoDaño(frenos)
admin.añadirTipoDaño(electrico)
admin.añadirTipoDaño(llantas)
admin.añadirTipoDaño(carroceria)

admin.setNombre("Julieta Vanegas")
admin.setId(1006784599)
admin.setMecanicos(mecanicos)
admin.setProveedores(proveedores)
admin.setInventario(inventario)
admin.setMecanicos(mecanicos)

picklefile = open("src/baseDatos/temp/pcs.pkl", "wb")

pickle.dump(admin, picklefile)

picklefile.close()






