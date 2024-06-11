from fastapi import APIRouter, Depends, Response
from controllers.auth_controller import AuthController
from auth.token import pega_token_do_cookie

#bycript para hash de senha

## Schemas
from schema.padrao_schema import Login, Token, Cadastro

router = APIRouter()

#observação resolver redundancia nos Schemas
@router.post("/cadastro", response_model = str)
async def cadastrar(info_cadastro: Cadastro):
    return AuthController.cadastrar(info_cadastro)

@router.post("/login", status_code=200)
async def login(info_login: Login, response : Response):
    return AuthController.login(info_login, response)

@router.get("/aluno", status_code=200)
async def aluno(token: str = Depends(pega_token_do_cookie)):
    return {"token":"funciona"}