from typing import Optional
from sqlmodel import Field,  SQLModel, Relationship, Column, String
from .credencial import Credencial


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    login: str = Field(sa_column=Column(String(30), nullable=False, unique=True))
    email: str  = Field(sa_column=Column(String(70), nullable=False, unique=True))
    senha: str = Field(sa_column=Column(String(100), nullable=False))
    tipo: int
    estado: int
    credencial: Credencial = Relationship(back_populates="usuario")

