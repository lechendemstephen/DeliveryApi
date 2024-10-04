from ..Database.database import Base
from sqlalchemy import Column, String, Integer

class SignUp(Base): 
    __tablename__ = 'signup'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
