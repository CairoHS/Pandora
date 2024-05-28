from datetime import timedelta, datetime, timezone
from typing import Union
import copy

import jwt
from schema.auth_schema import InfoToken

CHAVE_SECRETA = "972158c1b959ce309f667a3a9919bfe8c490ebf74c88a7347bf7f7065e094ad2"
ALGORITMO = "HS256"
MINUTOS_PARA_EXPIRAR_TOKEN = 30


def criar_token_acesso(info: InfoToken):
    info_copiada = info.model_copy()

    # calcula e adiciona tempo de expirar
    tempo_token = datetime.now(timezone.utc) + timedelta(minutes=MINUTOS_PARA_EXPIRAR_TOKEN)
    info_copiada.expirar = tempo_token
    
    #cria e manda token
    token_jwt = jwt.encode(info_copiada.model_dump(), CHAVE_SECRETA, algorithm=ALGORITMO)
    return token_jwt

