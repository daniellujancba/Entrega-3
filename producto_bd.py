

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


producto_1 = Producto(1,"casa",4, 10,"kg",4) 
print(producto_1.getnombre_Producto)
    
    