import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def obtener_conexion():
    conexion = psycopg2.connect(
        host= os.getenv("DB_HOST"),
        dbname= os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT")
    )
    return conexion

if __name__ == "__main__":
    conexion = obtener_conexion()
    print("Conexion exitosa!")
    conexion.close()