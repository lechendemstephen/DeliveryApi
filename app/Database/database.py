from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from ..config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.Database_name}:{settings.Database_password}@{settings.Database_host}/Delivery'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try: 
        yield db 
 
    finally: 
        db.close()
   

