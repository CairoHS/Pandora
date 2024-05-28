#enginer para a session
from sqlmodel import Session
from conn.conn import engine

# Schemas
from schema.auth_schema import Cadastro, Login, InfoToken, Token

#senha
from utils.encripta_senha import hash_senha, verificar_senha

# models
from models.credencial import Credencial
from models.usuario import Usuario

# comandos
from sqlmodel import select #select mysql
from sqlalchemy.orm import selectinload #pegar o filho junto

#converter para Json
from pydantic import Json

#opcoes para token
from utils.token import criar_token_acesso

class AuthController:
    def cadastrar(cadastro: Cadastro):
        with Session(engine) as session:
            try:

                usuario = Usuario(
                    login = cadastro.login,
                    senha = hash_senha(cadastro.senha),
                    email = cadastro.email,
                    tipo= 0,
                    estado = 0 )
                
                credencial = Credencial( 
                    usuario = usuario,
                    nome = cadastro.nome,
                    sobrenome = cadastro.sobrenome)

                session.add(usuario)
                session.add(credencial)

                session.commit()

            except Exception as e:

                session.rollback()
                raise e
        
        return f"salvo"
    
    def login(dados_login: Login):
        with Session(engine) as session:
           
           # pega dados do usuario e credencial
           query = select(Usuario).where(Usuario.login == dados_login.login).options(selectinload(Usuario.credencial))
           resultado = session.exec(query).first()

            # pega dados usados no token e faz
           dados_token =InfoToken.recebe_usuario_model(resultado)
           jwt_token = criar_token_acesso(dados_token)

           return Token(token_acesso=jwt_token, token_tipo = "Bearer")



           







