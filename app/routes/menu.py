from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.Database.database import get_db
from app.models.models import MenuItem, Category

from app import schemas


router = APIRouter(
    tags= ['Menu'],
    prefix= '/menu'

)


# creating menu category 
@router.post('/category')
async def create_category(request_category: schemas.Category, db: Session = Depends(get_db)): 

    new_category = Category(
        **request_category.dict()
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category





@router.post('/')
async def create_menu(request_item: schemas.Menu, db: Session = Depends(get_db)):


    new_item = MenuItem(
        **request_item.dict()
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item




