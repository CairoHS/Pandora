from fastapi import FastAPI
from .core import criar_banco
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Olá Mundo"}

if __name__ == "__main__":
    criar_banco()
