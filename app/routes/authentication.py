from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models.models import SignUp
from ..Database.database import get_db
from .. import schemas, utils, oath2

routers = APIRouter(
    tags=['Authentication']
)


@routers.post('/user')
async def create_user(user:schemas.SignUp, db: Session = Depends(get_db)): 
# checking if the user already exist 
    db_user = db.query(SignUp).filter(SignUp.email == user.email)

    if db_user is not None: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'user with email: {user.email}, already exist')

# hashing the password before sending to the database 
    hashed_password =  utils.has_password(user.password)
    user.password = hashed_password



    new_user = SignUp(
        **user.dict()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@routers.post('/login')
async def login_user(user:schemas.Login, db: Session = Depends(get_db)): 
    db_user = db.query(SignUp).filter(SignUp.email == user.email).first()

    if db_user is None: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid user credentials')
    
    if not utils.verify_password(user.password, db_user.password): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid user credentials')
    
    # create an access token 
    token = oath2.create_access_token({"user_id": db_user.id})


    return {
        "token": token
    }
    


    

