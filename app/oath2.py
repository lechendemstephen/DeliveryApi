from jose import jwt, JWTError
from datetime import datetime, timedelta
from .config import settings
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
