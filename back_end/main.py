from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from conn.conn import cria_banco
from routes import auth_routes
from schema.auth_schema import InfoToken
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

#rotas do fastapi
app.include_router(auth_routes.router)

#Para levantar os arquivos do front end
app.mount("/", StaticFiles(directory="../front_end", html=True), name="front_end")

cria_banco()