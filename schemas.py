from pydantic import BaseModel, EmailStr

class ContactoCreate(BaseModel):
    nombre: str
    telefono: str
    email: EmailStr
    direccion: str

class ContactoResponse(BaseModel):
    nombre: str
    telefono: str
    email: EmailStr
    direccion: str

class Config:
    from_attribute = True