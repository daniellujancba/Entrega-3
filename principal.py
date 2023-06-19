import Controlador_prod


while True:
    print("")
    print("")
    print("***********************************************************")
    print("******* Bienvenidos a la Base de Datos de Big Bread *******")
    print("***********************************************************")
    print("")
    print("MENU PRINCIPAL")
    print("")
    print("Seleccione una opcion: ")
    print("1 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCTO")
    print("2 - ALTA / BAJA / MODIFICACION DE INSUMOS")
    print("3 - ALTA / BAJA / MODIFICACION DE PRODUCCION DIARIA")
    print("4 - ALTA / BAJA / MODIFICACION DE RECETAS")
    print("5 - LISTADO DE PRODUCTOS")
    print("6 - LISTADO DE PRODUCCION EN UN INTERVALO")
    print("7 - LISTADO DE INSUMOS DIARIO")
    print("8 - SALIR")
    opcion =int(input("Ingrese su opcion: "))
    if opcion == 1:
        Controlador_prod.InsertarProducto()    
    

    elif opcion == 2:
        print("hola")

    elif opcion == 3:
        print("hola")

    elif opcion == 4:
        print("hola")

    elif opcion == 5:
        Controlador_prod.ListarProductos()

    elif opcion == 6:
        print("hola")

    elif opcion == 7:
        print("hola")

    elif opcion == 8:
            break
    else:
        print("Opcion Incorrecta!!!")



    