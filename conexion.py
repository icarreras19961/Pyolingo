import mariadb
import sys
# Un intento por hacer el codigo estructurado y que no se repitan cosas pero funciona un poco tinkiwinki
def conexion():
    try:
        conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="pyolingo"
        )
        return conn
    except mariadb.Error as e:
        print("Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

