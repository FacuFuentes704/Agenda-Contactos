from database import obtener_conexion
import psycopg2.extras

class Contacto():
    def __init__(self, id, nombre, telefono, email, direccion):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
    
    def __str__(self):
        return f"Nombre: {self.nombre} | Telefono: {self.telefono} | Email: {self.email} | Direccion: {self.direccion}"

class Agenda:
    def __init__(self):
           pass
    def agregar_contactos(self, nombre, telefono, email, direccion):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO contactos (nombre, telefono, email, direccion) VALUES (%s, %s, %s, %s)"
        values = (nombre, telefono, email, direccion)
        try:
            cursor.execute(query, values)
            conexion.commit()
            return True
        except Exception as e:
            print("No se pudo realizar la peticion", e)
            return False
        finally:
            conexion.close()
        
    def buscar_contactos(self, nombre):
        contactos = []
        conexion = obtener_conexion()
        cursor = conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM contactos WHERE LOWER(nombre) = LOWER(%s)"
        values = (nombre,)
        try:
            cursor.execute(query, values)
            resultados = cursor.fetchall()
            for contacto in resultados:
                nuevo_contacto = Contacto(contacto["id"], contacto["nombre"], contacto["telefono"], contacto["email"], contacto["direccion"])
                contactos.append(nuevo_contacto)
            return contactos
        except Exception as e:
            print("Error", e)
            return
        finally:
            conexion.close()
    
    def eliminar(self, eleccion):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM contactos WHERE ID = %s"
        values = (eleccion,)
        try:
            cursor.execute(query, values)
            conexion.commit()
            return True
        except Exception as e:
            print("ERROR!", e)
            return False
        finally:
            conexion.close()

    def listar_contactos(self):
        contactos = []
        conexion = obtener_conexion()
        cursor = conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM contactos"
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            for contacto in resultado:
                nuevo_contacto = Contacto(contacto["id"], contacto["nombre"], contacto["telefono"], contacto["email"], contacto["direccion"])
                contactos.append(nuevo_contacto)
            return contactos
        except Exception as e:
            print("Error!", e)
            return

def eliminar_contacto():
    opciones = "si", "no"
    nombre = recibir_contacto()
    if nombre is None:
        print("Resultados Incompletos")
        return
    resultado = mi_agenda.buscar_contactos(nombre)
    if not resultado:
        print("El nombre no se encuentra en la base de datos!")
        return
    for indice, contacto in enumerate(resultado, start=1):
        print(indice, contacto)
    try:
        respuesta = int(input("Ingrese el indice del contacto a eliminar"))
    except ValueError:
        print("Respuesta invalida")
        return
    if respuesta < 1 or respuesta > len(resultado):
        print("Indice incorrecto!")
        return
    eleccion = resultado[respuesta - 1]
    print("El contacto a eliminar es el siguiente?")
    print(eleccion)
    while True:
        respuesta2 = input("Ingrese la respuesta SI/NO").lower()
        if respuesta2 not in opciones:
            print("No ingresaste una respuesta valida!")
            continue
        if respuesta2 == "no":
            print("Opcion cancelada")
            break
        if respuesta2 == "si":
            mi_agenda.eliminar(eleccion.id)
            print("Usuario eliminado con exito!")
            return

def recibir_contacto():
    nombre = input("Escriba el nombre del contacto").lower()
    if not nombre:
        print("Datos incompletos")
        return
    return nombre

def crear_contacto():
    nombre = input("Ingrese un nombre").strip()
    email = input("Ingrese un email").strip()
    if "@" not in email or "." not in email:
        print("No ingresaste un formato valido de email")
        return
    direccion = input("Ingrese su direccion").strip()
    try:    
        telefono = int(input("Ingrese un telefono").strip())
    except ValueError as e:
        print("No ingresaste un numero!")
        return
    if not nombre or not direccion:
        print("Datos incompletos")
        return
    return nombre, telefono, email, direccion

def buscar():
    nombre = recibir_contacto()
    if nombre is None:
        print("Resultado vacio")
        return
    resultado = mi_agenda.buscar_contactos(nombre)
    for contacto in resultado:
        print(contacto)

def validar_datos():
    resultado = crear_contacto()
    if resultado is None:
        print("Resultados incompletos")
    else:
        mi_agenda.agregar_contactos(*resultado)

def listar():
    resultado = mi_agenda.listar_contactos()
    for indice, contacto in enumerate(resultado, start=1):
        print(indice, contacto)

mi_agenda = Agenda()

def mostrar_menu():
    print("Opcion 1: Agregar usuario")
    print("Opcion 2: Buscar usuario")
    print("Opcion 3: Eliminar usuario")
    print("Opcion 4: Listar usuarios")
    print("Opcion 5: Salir")


def menu():
    opciones = {1: validar_datos,
              2: buscar,
              3: eliminar_contacto,
              4: listar
        }
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opcion"))
        except ValueError:
            print("Datos incorrectos!")
            continue
        if opcion in opciones:
            opciones[opcion]()
        elif opcion == 5:
            print("Hasta la proxima!")
            break
        else:
            print("Opcion invalida!")
            continue

menu()
        

    
        