from pydantic import BaseModel
from typing import Any, Union, Optional
from datetime import  datetime

# pega modelo do banco porque tb é um pydantic, e vai ser usado no token
from models.usuario import Usuario

# usado para sistema validar sistema de cadastro
class Cadastro(BaseModel):
    nome: str
    sobrenome: str
    email: str
    login: str
    senha: str

# usado para sistema validar sistema de login
class Login(BaseModel):
    login: str
    senha: str


# para token jwt 
class InfoToken(BaseModel):
    email: str
    nome: str
    sobrenome: str
    expirar: Optional[datetime] = None
    
    @classmethod
    def recebe_usuario_model(cls, modelo: Usuario):
        email = modelo.email
        nome = modelo.credencial.nome
        sobrenome = modelo.credencial.sobrenome
        return InfoToken(email= email, nome=nome,sobrenome =sobrenome, )

class Token(BaseModel):
    token_acesso: str
    token_tipo: str







    