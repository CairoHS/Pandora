from pydantic import BaseModel

class Cadastro(BaseModel):
    nome: str
    sobrenome: str
    email: str
    usuario: str
    senha: str