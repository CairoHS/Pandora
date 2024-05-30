from fastapi import HTTPException, status

def excecao401_nao_autorizado(detalhes: str = "Não Autorizado"):
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail= detalhes
    )

def excecao404_nao_encontrado(detalhes: str = "Item não Encontrado"):
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = detalhes
    )
