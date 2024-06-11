import uvicorn
import logging
from fastapi import FastAPI, Request
#from fastapi.staticfiles import StaticFiles
from conn.conn import cria_banco
from routes import auth_routes
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(filename='app.log', level=logging.ERROR)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request : Request, exc: Exception):
    logging.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )



#rotas do fastapi
app.include_router(auth_routes.router)

#Para levantar os arquivos do front end
#app.mount("/", StaticFiles(directory="../front_end", html=True), name="front_end")

cria_banco()