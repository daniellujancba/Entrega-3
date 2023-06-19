
# Esta es la interfase que armamos para e usuario

import Modelo

def ListarProductos():
    com = Modelo.Conectar()

    listado = com.ListarProductos()

    print("\n! ID PRODUCTO  !  NOMBRE PRODUCTO  !  STOCK  !  PRECIO  !  UNIDAD DE MEDIDA  !  RECETA")

    for producto in listado:
        print("  ",producto[0],"\t\t",producto[1],"\t\t",str(producto[2])+"\t\t$"+str(producto[3]),"\t\t",producto[4],"\t\t",producto[5]) #falta comleetar el print
        input("Para continuar presione enter")



ListarProductos()


def InsertarProducto():
    com = Modelo.Conectar()


    nombre_Producto = input("\nIngrese el nombre del Producto: ")
    stock = int(input("\nIngrese el stock del Producto: "))
    precio = int(input("\nIngrese el precio del Producto: "))
    unidad_de_medida = input("\nIngrese la unidad de medida del Producto: ")

    nuevo_Producto = Modelo.Producto(0,nombre_Producto,stock,precio,unidad_de_medida,0)

    com.InsertarProducto(nuevo_Producto)
    input("Para continuar presione enter")

#InsertarProducto()


