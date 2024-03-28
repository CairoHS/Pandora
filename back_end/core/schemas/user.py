import datetime
from conn.conn import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_columm
from sqlalchemy import String
from sqlalchemy import Integer


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_columm(primary_key=True)
    email: Mapped[str] = mapped_columm(String(45), nullable=False)
    senha: Mapped[str] = mapped_columm(String(50), nullable=False)
    status: Mapped[int] = mapped_columm(Integer(2))
    ultimoLogin: Mapped[datetime.datetime]
