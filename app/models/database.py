from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener valores de las variables de entorno
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")

urlConection = f"mysql+mysqlconnector://{DB_USER}:@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(urlConection)


def createDbAndTables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session
