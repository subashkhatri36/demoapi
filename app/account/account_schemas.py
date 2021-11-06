from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    fullname:str
    email:str
    password:str
    profile:str
    last_login:datetime
    is_superuser:bool
    is_staff:bool
    date_joined:datetime
    is_active:bool

class MainUser(BaseModel):
    fullname:str
    email:str
    password:str
   
   

class ShowUser(BaseModel):   
    fullname:str
    email:str
    profile:str
    last_login:datetime
    is_superuser:bool
    is_staff:bool
    date_joined:datetime
    is_active:bool

    class Config():
        orm_mode = True



        

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None