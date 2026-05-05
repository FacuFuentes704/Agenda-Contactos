class Contacto():
    def __init__(self, nombre, telefono, email, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
    
    def __str__(self):
        return f"Nombre: {self.nombre} | Telefono: {self.telefono} | Email: {self.email} | Direccion: {self.direccion}"

class Agenda:
    def __init__(self):
        self.contactos = []
    
    def agregar_contactos(self, nombre, telefono, email, direccion):
        nuevo_contacto = Contacto(nombre, telefono, email, direccion)
        self.contactos.append(nuevo_contacto)
        
    def buscar_contactos(self, nombre):
        resultado = []
        for contacto in self.contactos:
            if nombre == contacto.nombre.lower():
                resultado.append(contacto)
        if not resultado:
            print("No se encontro el contacto")
        return resultado
    
    def eliminar(self, eleccion):
        self.contactos.remove(eleccion)

def eliminar_contacto():
    opciones = "si", "no"
    nombre = recibir_contacto()
    if nombre is None:
        print("Resultados Incompletos")
        return
    resultado = mi_agenda.buscar_contactos(nombre)
    for indice, contacto in enumerate(resultado, start=1):
        print(indice, contacto)
    try:
        respuesta = int(input("Ingrese el indice del contacto a eliminar"))
    except ValueError:
        print("Respuesta invalida")
        return
    eleccion = resultado[respuesta - 1]
    print("El contacto a eliminar es el siguiente?")
    print(eleccion)
    respuesta2 = input("Ingrese la respuesta").lower()
    if respuesta2 not in opciones:
        print("No ingresaste una respuesta valida!")
        return
    if respuesta2 == "no":
        print("Opcion cancelada")
        return
    if respuesta2 == "si":
        mi_agenda.eliminar(eleccion)

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

mi_agenda = Agenda()

def mostrar_menu():
    print("Opcion 1: Agregar usuario")
    print("Opcion 2: Buscar usuario")
    print("Opcion 3: Eliminar usuario")
    print("Opcion 4: Modificar usuario")
    print("Opcion 5: Salir")


def menu():
    opciones = {1: validar_datos,
              2: buscar,
              3: eliminar_contacto
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
        

    
        