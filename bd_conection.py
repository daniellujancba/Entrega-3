import mysql.connector


class Conectar_Base_Innova():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.conector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "1234",
                db = "bd_big_bread"
            )
        except mysql.connector.Error as descripcionerror:
            print("No se conecto la base de datos",descripcionerror)







