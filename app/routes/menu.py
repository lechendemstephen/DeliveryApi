from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.Database.database import get_db
from app.models.models import MenuItem, Category

from app import schemas


router = APIRouter(
    tags= ['Menu'],
    prefix= '/menu'

)


# creating menu category___________________________________________________________________________start

@router.get('/category')
async def all_categories(db: Session = Depends(get_db)): 
    all_categories = db.query(Category).all()
    return all_categories
 
    
@router.post('/category')
async def create_category(request_category: schemas.Category, db: Session = Depends(get_db)): 

    new_category = Category(
        **request_category.dict()
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

@router.put('/category/{id}')
async def update_category(request_cat: schemas.Category , id: int, db: Session = Depends(get_db)): 
    cat = db.query(Category).filter(Category.id == id).first()

    if not cat: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no category found with provided ID')
    
    for key, values in request_cat.dict().items(): 
        if values is not None: 
            setattr(cat, key, values)
    db.add(cat)
    db.commit()
    db.refresh(cat)

    return cat

@router.get('/category/{id}')
async def get_category(id: int, db: Session = Depends(get_db)): 
    get_cat = db.query(Category).filter(Category.id == id).first()

    if not get_cat: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no category with ID found')


    return get_cat


@router.delete('/category/{id}')
async def delete_category(id: int, db: Session = Depends(get_db)): 
    del_cat = db.query(Category).filter(Category.id == id).first()

    if not del_cat: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no category with ID found')
    db.delete(del_cat)
    db.commit()

    return del_cat

#end of category CRUD_________________________________________________________________________________end



@router.get('/')
async def get_all_menu(db: Session = Depends(get_db)): 
    all_menu = db.query(MenuItem).filter(MenuItem.is_available==True).all()

    return all_menu



@router.post('/')
async def create_menu(request_item: schemas.Menu, db: Session = Depends(get_db)):


    new_item = MenuItem(
        **request_item.dict()
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

@router.put('/{id}')
async def update_menu(up_menu: schemas.Menu, id: int, db: Session = Depends(get_db)): 
    update_menu = db.query(MenuItem).filter(MenuItem.id == id).first()

    for key, value in up_menu.dict().items(): 
        if value is not None: 
            setattr(update_menu, key, value)
    db.add(update_menu)
    db.commit()
    db.refresh(update_menu)

    return update_menu


@router.get('/{id}')
async def get_menu_item(id: int, db: Session = Depends(get_db)): 
    menu_item = db.query(MenuItem).filter(MenuItem.id == id).first()

    if not menu_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='menu item not found')
    
    return menu_item

@router.delete('/{id}')
async def get_menu_item(id: int, db: Session = Depends(get_db)): 
    menu_item = db.query(MenuItem).filter(MenuItem.id == id).first()

    if not menu_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='menu item not found')
    
    db.delete(menu_item)
    db.commit()
    db.refresh(menu_item)

    return menu_item








