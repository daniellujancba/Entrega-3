import mysql.connector


class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = input("Ingrese el Usuario: "), # root
                password = input("Ingrese el Password: "),# " " - vacio + enter
                db= input("Ingrese el nombre de la Base de Datos: ")
            )
            if self.conexion.is_connected():
                print("")
                print("LA CONEXION ES EXITOSA")
                print("")
                
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    def traer_db(self):   # MUESTRA EL LISTADO DE BASES EN MYSQL     
        try:
            if self.conexion.is_connected():
                print("esta conectado")       
                mi_cursor = self.conexion.cursor()
                print("Para mostrar el listado de bases de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) # SHOW DATABASES
                mi_cursor.execute(query)
                for db in mi_cursor:
                    print (db)
            
                mi_cursor.close()
                self.conexion.close()          
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS") 

    def crear_db(self): #CREA UNA BASE DE DATOS EN MYSQL
        try:
            if self.conexion.is_connected():
                print("esta conectado")       
                mi_cursor = self.conexion.cursor()
                print("Para crear un BD en el listado de bases de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) # SHOW DATABASES
                mi_cursor.execute(query)           
                mi_cursor.close()
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")  


        


##############################################################################################
"""
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

    """