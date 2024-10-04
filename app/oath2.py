from jose import jwt, JWTError
from datetime import datetime, timedelta
from .config import settings
from . import schemas
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

oath2_schemes = OAuth2PasswordBearer(tokenUrl='login')

#SECRET_KEY
#ALGORITHM
#ACCESS_TOKEN_EXPIRE_MINUTES 

# function to create an access token 
def create_access_token(data: dict): 
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.Access_token_expire_minutes)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.Secret_key, algorithm=settings.Algorithm)

    return encoded_jwt

# function to verify the access token 
def verify_access_token(token:str, credential_exception): 
    try : 
        payload = jwt.decode(token, settings.Secret_key, algorithms=settings.Algorithm)
    except: 
        raise credential_exception
    id: str = payload.get('user_id')
    if not id: 
        raise JWTError 
    token_data = schemas.TokenData(token_data=str(id))

    return token_data

# function to get the current authenticated user 
def get_current_user(token: str = Depends(oath2_schemes)): 
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid token')

    return verify_access_token(token, credential_exception)

