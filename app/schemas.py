from pydantic import BaseModel, EmailStr



class SignUp(BaseModel): 
    name: str 
    email: EmailStr
    password: str 

class Login(BaseModel): 
    email: EmailStr 
    password: str 

class TokenData(BaseModel): 
    token_data: str 




class Category(BaseModel): 
    name:str 


class Menu(BaseModel): 
    name: str 
    category: int 
    price: int 
    is_available: bool


