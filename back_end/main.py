from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.conn.conn import criar_banco


app = FastAPI()


app.mount("/", StaticFiles(directory="../front_end", html=True), name="front_end")


if __name__ == "__main__":
    criar_banco()
