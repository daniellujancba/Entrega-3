from conexion_bd_2 import Conectar

print("")
print("")
print("***********************************************************")
print("******* Bienvenidos a la Base de Datos de Big Bread *******")
print("***********************************************************")
print("")
print("Para acceder debera ingresar su Usuario y Password y elegir una Base de Datos")
tor = Conectar()
print("Desea realizar una consulta?")
eleccion = str(input("Ingrese -y- en caso afirmativo o -n- en caso negativo: "))
if eleccion == "y":
    print("")
    print("Seleccione una opcion: ")
    print("1 - Ver bases de datos")
    print("2 - Crear una BD")
    print("3 - Eliminar un BD")
    print("4 - Ver tablas en BD")
    print("5 - Crear tabla en BD")
    print("6 - Eliminar tabla en BD")
    print("7 - Insertar insumo en Tabla")
    print("8 - Listado de insumos")

    opcion = str(input("Ingrese numero: "))
    if opcion == "1":
        tor.traer_db()
        
    elif opcion == "2":
        tor.crear_db()
