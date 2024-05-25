from typing import Optional
from sqlmodel import Field,  SQLModel, Column, String, Relationship


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario: str = Column(String(length=30), nullable=False)
    email: str  = Column(String(length=70), nullable=False)
    senha: str = Column(String(length=25), nullable=False)
    tipo: int
    estado: int
    # relacionamento no SQLModel
    credenciais: Optional["Credential"] = Relationship(back_populates="usuario")

