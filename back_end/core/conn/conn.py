from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from .end import url_object

# Conexão com o banco de Dados
engine = create_engine(url_object)

# variavel para dar commit para o banco
session = Session(engine)


# classe base para criar os bancos de dados
class Base(DeclarativeBase):
    pass
