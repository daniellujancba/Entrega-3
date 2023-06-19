
# este metodo es para ir a la base de datos a uscar los datos
import mysql.connector
from mysql.connector import Error

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = "3306", # 3306
                user = "root", # root
                password = "",# " " - vacio + enter
                db= "big_bread"
            )
            if self.conexion.is_connected():
                print("")
                print("LA CONEXION ES EXITOSA")
                print("")
                
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")

    
    
    def InsertarProducto(self,producto): # INSERTAR UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 9
        
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                query = "INSERT INTO productos VALUES(null,%s, %s, %s, %s,null)"
                #query = str(input("Ingrese la sentencia en mayuscula:"))
                #query = "INSERT INTO producto(iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (producto.getnombre_Producto(),
                        producto.getstock(),
                        producto.getprecio(),
                        producto.getunidad_de_medida()
                        )
                mi_cursor.execute(query,data)
                self.conexion.commit()
                print("Producto insertado correctamente")
                
                mi_cursor.close()

                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")

    def ListarProductos(self): # SELECCIONAR UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 10
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                print("Informacion de los  productos")
                #query = str(input("Ingrese la sentencia en mayuscula:")) #SELECT * FROM Productos
                query = "SELECT * FROM producto"
                mi_cursor.execute(query)
                resultados= mi_cursor.fetchall()
                mi_cursor.close()
                return resultados
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")    

    def UpdateProducto(self,condicion):
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                
                query = "UPDATE producto SET precio = 20 WHERE {condicion} "
                mi_cursor.execute(query)
                self.conexion.commit()
                print("Producto actualizado correctamente")
                print("conexion")
                mi_cursor.close()

                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")

    def DeleteProducto(self):
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                
                query = "DELETE FROM producto WHERE iD_Producto = 1"
                mi_cursor.execute(query)
                self.conexion.commit()
                print("El Producto se ha eliminado")
                
                mi_cursor.close()

                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


#a = str("nombre_Producto = factura")
DeleteProducto()



class Producto():
    ID_Producto =0,
    Nombre_Producto = "",
    Stock =0,
    Precio = 0,
    Unidad_de_medida = "",
    ID_Receta = 0

    def __init__(self,iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta):
        self.ID_Producto = iD_Producto 
        self.Nombre_Producto =nombre_Producto
        self.Stock = stock
        self.Precio = precio
        self.Unidad_de_medida=unidad_de_medida
        self.ID_Receta =iD_Receta
    
    def getiD_Producto(self): #el objetivo de este metodo es obtener el valor de este en especifico; ID_PRODUCTO
        return self.iD_Producto
    def getnombre_Producto(self):
        return self.nombre_Producto
    def getstock(self):
        return self.stock
    def getprecio(self):
        return self.precio
    def getunidad_de_medida(self):
        return self.unidad_de_medida
    def getiD_Receta(self):
        return self.iD_Receta
    
    def setiD_Producto(self,iD_Producto):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.iD_Producto = iD_Producto
    def setnombre_Producto(self,nombre_Producto):
        self.nombre_Producto = nombre_Producto
    def setstock(self,stock):
        self.stock = stock
    def setprecio(self,precio):
        self.precio = precio
    def setunidad_de_medida(self,unidad_de_medida):
        self.unidad_de_medida = unidad_de_medida
    def setiD_Receta(self,iD_Receta):
        self.iD_Receta = iD_Receta   
 
    

    
   