from pydantic_settings import BaseSettings 


class Settings(BaseSettings): 
    Database_name: str
    Database_password: str 
    Database_host: str 
    Secret_key:str 
    Algorithm: str 
    Access_token_expire_minutes: int 

    class Config: 
        env_file = '.env'

settings = Settings()