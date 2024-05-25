from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from conn.conn import criar_banco
from routes import auth_routes


app = FastAPI()

app.mount("/", StaticFiles(directory="../front_end", html=True), name="front_end")

app.include_router(auth_routes.router)

if __name__ == "__main__":
    criar_banco()
