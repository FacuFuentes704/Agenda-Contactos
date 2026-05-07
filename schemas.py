from pydantic import BaseModel, EmailStr, Field

class ContactoCreate(BaseModel):
    nombre: str = Field(min_length=1)
    telefono: str = Field(min_length = 1)
    email: EmailStr = Field(min_length=1)
    direccion: str = Field(min_length=1)

class ContactoResponse(BaseModel):
    nombre: str = Field(min_length=1)
    telefono: str = Field(min_length = 1)
    email: EmailStr = Field(min_length=1)
    direccion: str = Field(min_length=1)

class Config:
    from_attribute = True