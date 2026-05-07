from fastapi import FastAPI, HTTPException
from contactos import Agenda, mi_agenda
from schemas import ContactoCreate, ContactoResponse

app = FastAPI()

@app.get("/")
def inicio():
    return{"Mensaje": "Bienvenido a la API de agenda"}

@app.get("/contactos", response_model=list[ContactoResponse])
def listar_contactos():
    resultado = mi_agenda.listar_contactos()
    return resultado

@app.post("/contactos", response_model=ContactoResponse)
def agregar_contacto(contacto: ContactoCreate):
    mi_agenda.agregar_contactos(contacto.nombre, contacto.telefono, contacto.email, contacto.direccion)
    return contacto

@app.get("/contactos/{nombre}", response_model=list[ContactoResponse])
def buscar_contactos(nombre: str):
    resultado = mi_agenda.buscar_contactos(nombre)
    if not resultado:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    else:
        return resultado

@app.delete("/contactos/{id}")
def eliminar(id: int):
    resultado = mi_agenda.eliminar(id)
    if resultado is False:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    else:
        return{"mensaje": "Contacto eliminado con exito"}

