from sqlalchemy import URL

url_object = URL.create(
    "postgresql+psycopg2",
    username="",
    password="",
    host="",
    database="",
)
