# metodo .connect(base.db) ----> sirve para crear base de datos 
# metodo .Error y lo renombre err
import sqlite3

def conectar():
    try:
        conexion = sqlite3.connect('contactos.db')
        print('Se ha conectado a la base de datos')
        return conexion
    except sqlite3.Error as err:#La clase base de otras excepciones en este módulo. Es una subclase de Exception
        print('Ha ocurrido un error', err)

def crear_tabla(conexion):
    cursor = conexion.cursor()
    sentencia_sql = ''' CREATE TABLE IF NOT EXISTS contacto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        empresa TEXT NOT NULL,
        telefono TEXT NOT NULL,
        email TEXT NOT NULL,
        direccion TEXT NULL
    ) '''
    cursor.execute(sentencia_sql)
    conexion.commit() #Guardamos los cambios al terminar el ciclo