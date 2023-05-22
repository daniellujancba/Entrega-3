import mysql.conector


class Conectar_Base_Innova():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.conector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "admin",
                db = "bd_ejemplo_innova"
            )
        except mysql.connector.Error as descripcionerror:
            print("No se conecto la base de datos",descripcionerror)



