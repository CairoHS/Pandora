from typing import Optional

from sqlmodel import Field,  SQLModel


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    senha: str
