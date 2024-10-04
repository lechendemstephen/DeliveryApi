from fastapi import FastAPI
from .routes import authentication, menu, order
from .models import models 
from .Database.database import Base, engine


Base = models.Base.metadata.create_all(bind=engine)
app = FastAPI()



app.include_router(authentication.routers)
app.include_router(menu.router)
app.include_router(order.router)

