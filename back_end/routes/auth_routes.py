from fastapi import APIRouter
from controllers.auth_controller import AuthController, Login

#bycript para hash de senha

## Schemas
from schema.auth_schema import Cadastro

router = APIRouter()

#observação resolver redundancia nos Schemas
@router.post("/cadastro")
async def cadastrar(info_cadastro: Cadastro):
    return AuthController.cadastrar(info_cadastro)

@router.post("/login")
async def login(info_login: Login):
    return AuthController.login(info_login)