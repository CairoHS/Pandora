from fastapi import APIRouter, Depends
from controllers.auth_controller import AuthController
from auth.token import authentica_token_acesso

#bycript para hash de senha

## Schemas
from schema.padrao_schema import Login, Token, Cadastro

router = APIRouter()

#observação resolver redundancia nos Schemas
@router.post("/cadastro")
async def cadastrar(info_cadastro: Cadastro):
    return AuthController.cadastrar(info_cadastro)

@router.post("/login", response_model = Token)
async def login(info_login: Login):
    return AuthController.login(info_login)

@router.post("/aluno")
async def aluno(token: str = Depends(authentica_token_acesso)):
    return {"token":"funciona"}