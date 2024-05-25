#enginer para a session
from sqlmodel import Session
from conn.conn import engine
# Schemas
from schema.auth_schema import Cadastro

# models
from models.credencial import Credencial
from models.usuario import Usuario


class AuthController:
    def cadastrar(cadastro: Cadastro):
        with Session(engine) as session:
            try:

                usuario = Usuario(**cadastro.model_dump, tipo=0, estado=0)
                credencial = Credencial(**cadastro.model_dump,usuario=usuario)

                session.add(usuario)
                session.add(credencial)

                session.commit()

            except Exception as e:

                session.rollback()
                raise e
        
        return f"salvo"







