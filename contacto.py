from conexion import *

def registrar(nombre, apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO contacto(nombre, apellidos, empresa, telefono, email, direccion) values ( ?, ?, ?, ?, ?, ? ) '''
        datos = (nombre, apellidos, empresa, telefono, email, direccion)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()#Este método cierra la conexión a la base de datos. Nótese que éste no llama automáticamente commit()
        return 'Registro correcto'
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contacto ''' 
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()#recupera todas las filas del resultado de una consulta. Devuelve todas las filas como una lista de tuplas. Se devuelve una lista vacía si no hay ningún registro que recuperar
        con.close()
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)
    return datos

def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = '''SELECT * FROM contacto WHERE id=?'''
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print('Ha ocrrido un error', err)
    return datos

def modificar(id, nombre, apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql  = ''' UPDATE contacto SET nombre=?, apellidos=?, empresa=?, telefono=?, email=?, direccion=? WHERE id=? '''
        datos = (nombre, apellidos, empresa, telefono, email, direccion, id)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return "Se actualizó correctamente"
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)

def eliminar(id):
    try:
        con = conectar()
        cursor= con.cursor()
        sentencia_sql = '''DELETE FROM contacto where id=?'''
        cursor.execute(sentencia_sql, (id,))
        con.commit()
        con.close()
        return "Se eliminó correctamente"
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)