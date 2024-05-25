from typing import Optional
from sqlmodel import SQLModel, Field, Column, String, Relationship

#tabela usuario para conectar no codigo
from .usuario import Usuario

class Credencial(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Column(String(length=45))
    sobrenome: str = Column(String(length=150))
    id_usuario: int | None = Field(default=None, foreign_key="usuario.id")
    usuario: Usuario = Relationship(back_populates="credencial")

