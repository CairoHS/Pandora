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
    atualizar:Optional[float]= 0
    expirar: Optional[float] = 0
    
    @classmethod
    def recebe_usuario_model(cls, modelo: Usuario) -> 'InfoToken':
        email = modelo.email
        nome = modelo.credencial.nome
        sobrenome = modelo.credencial.sobrenome
        return InfoToken(email= email, nome=nome,sobrenome =sobrenome )
    
    def testa_token(self, outro_token :'InfoToken', tempo_comparar: float) -> bool:
        if self.email != outro_token.email:
            return False
        if self.nome != outro_token.nome:
            return False
        if self.sobrenome != outro_token.sobrenome:
            return False
        print(self.expirar, tempo_comparar, self.expirar - tempo_comparar)
        if self.expirar < tempo_comparar:
            return False
        
        return True
    
    def atualizar_token(self, tempo: float) -> bool:
        if self.atulizar < tempo:
            return True
        return False


class Token(BaseModel):
    token_acesso: str
    token_tipo: str







    