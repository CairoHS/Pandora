from sqlmodel import SQLModel, create_engine
from .endereco import url

url_banco = f"mysql+mysqlconnector://{url}"

engine = create_engine(url_banco)


def criar_banco():
    SQLModel.metadata.create_all(engine)
