from sqlmodel import SQLModel, create_engine
from .endereco import url

from models.credencial import Credencial
from models.usuario import Usuario

url_banco = url

engine = create_engine(url_banco)

def cria_banco():
    try:
        SQLModel.metadata.create_all(engine)

    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    
