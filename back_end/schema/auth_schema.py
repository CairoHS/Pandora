from pydantic import BaseModel

class Cadastro(BaseModel):
    nome: str
    sobrenome: str
    email: str
    login: str
    senha: str

class Login(BaseModel):
    login: str
    senha: str