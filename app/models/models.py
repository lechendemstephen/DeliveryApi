from ..Database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, BigInteger, Boolean

class SignUp(Base): 
    __tablename__ = 'signup'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    jioned_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=('now()'))


class Category(Base): 
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=('now()'))

class MenuItem(Base): 
    __tablename__ = 'menuitem'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    category = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'), unique=True)
    price = Column(BigInteger, nullable=False)
    is_available = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=('now()'))



