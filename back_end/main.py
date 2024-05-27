from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from conn.conn import cria_banco
from routes import auth_routes




app = FastAPI()

app.include_router(auth_routes.router)

app.mount("/", StaticFiles(directory="../front_end", html=True), name="front_end")

cria_banco()