from fastapi import APIRouter
from controllers.auth_controller import AuthController


router = APIRouter()

@router.post("/cadastro/")
async def cadastrar(info_cadastro):
    return AuthController.cadastrar(info_cadastro)