#erro do fastapi
from fastapi import HTTPException, Depends

#enginer para a session
from sqlmodel import Session
from conn.conn import engine

# models
from models.credencial import Credencial
from models.usuario import Usuario



# comandos
from sqlmodel import select #select mysql
from sqlalchemy.orm import selectinload #pegar o filho junto

from datetime import timedelta, datetime, timezone
from typing import Union

import jwt
from schema.padrao_schema import InfoToken

#Segurança

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

CHAVE_SECRETA = "972158c1b959ce309f667a3a9919bfe8c490ebf74c88a7347bf7f7065e094ad2"
ALGORITMO = "HS256"
HORAS_PARA_EXPIRAR_TOKEN = 24
MINUTOS_PARA_ATUALIZAR_TOKEN = 15 



def criar_token_acesso(info: InfoToken):
    info_copiada = info.model_copy()

    # calcula e adiciona tempo de expirar
    tempo_expirar = (datetime.now(timezone.utc) + timedelta(hours= HORAS_PARA_EXPIRAR_TOKEN)).timestamp()
    info_copiada.expirar = tempo_expirar

    tempo_atualizar = (datetime.now(timezone.utc) + timedelta(minutes= MINUTOS_PARA_ATUALIZAR_TOKEN)).timestamp()
    info_copiada.atualizar = tempo_atualizar
    

    #cria e manda token
    token_jwt = jwt.encode(info_copiada.model_dump(), CHAVE_SECRETA, algorithm=ALGORITMO)

    return token_jwt


def authentica_token_acesso(token: str = Depends(oauth2_scheme)):
    dados_token = InfoToken(**jwt.decode(token, CHAVE_SECRETA, algorithms=[ALGORITMO]))

    with Session(engine) as session:
           
           # pega dados do usuario e credencial
           query = select(Usuario).where(Usuario.email == dados_token.email).options(selectinload(Usuario.credencial))
           resultado = session.exec(query).first()

            # pega dados usados e cria o token
           token_db =InfoToken.recebe_usuario_model(resultado)
           
           tempo_expirar = (datetime.now(timezone.utc) - timedelta(hours= HORAS_PARA_EXPIRAR_TOKEN)).timestamp()
           
           # compara dados dos token
           if not dados_token.testa_token(token_db, tempo_expirar):
                raise HTTPException(
                    status_code=401, 
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"}
                )
           

           return dados_token.model_dump()
           

def atualiza_token(token: str) -> str:
    dados_token = InfoToken(**jwt.decode(token, CHAVE_SECRETA, algorithms=[ALGORITMO]))

    tempo_atualizar = (datetime.now(timezone.utc) - timedelta(minutes= MINUTOS_PARA_ATUALIZAR_TOKEN)).timestamp()
    
    if dados_token.atualizar_token(tempo_atualizar):
         dados_token.atualizar = tempo_atualizar
         novotoken = jwt.encode(dados_token.model_dump, CHAVE_SECRETA, algorithm=ALGORITMO)

    return dados_token
    




         
         



