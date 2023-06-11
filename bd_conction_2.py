# probar metodo de conexion sin clases

import mysql.connector
# genero objeto mi conexion

# importo el paquete de errores de mysql

from mysql.connector import Error

# aplico el metodo try-except

try:
    mi_conexion = mysql.connector.connect(
    host = "localhost",
    user = input("ingrese el ususario: "),
    password = input("ingrese el password: ")
    )
# verifico que la conexion este presente
    if mi_conexion.is_connected():
        print("usted esta conectado")

# genero un cursor para realizar querys

    mi_cursor = mi_conexion.cursor()

# formulo la consulta que quiero hacer con el metodo execute
# Primero pregunto las bases de datos que hay
    mi_cursor.execute("SHOW DATABASES") #es un objeto para iterar, es una serie

    for DATABASES in mi_cursor:
        print(DATABASES)



# cierro del cursor

    mi_cursor.close()

# cierro la conexion
    mi_conexion.close()
# verifico que la conexion este cerrada
    if not mi_conexion.is_connected():
        print("la conexion esta cerrada")

except Error as e:
    print("ha ocurrido un error")
    print(e)

