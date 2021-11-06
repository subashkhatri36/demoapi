from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class CompnayBase(BaseModel):
    company_name:str
    user_id:int
    company_email:str
    company_contact :str
    company_address:str
    company_logo :str
    company_pan :str
    comapny_description:str
    owner_citizenship:str  
    branch:bool
    active:bool
    create_at:datetime
    updated_at:datetime

class Company(CompnayBase):
    class Config():
        orm_mode=True


class ShowCompany(BaseModel):
    company_name:str
    company_email:str
    company_contact :str
    company_address:str
    company_logo :str
    company_pan :str
    comapny_description:str
    owner_citizenship:str  
    user_id:int
    branch:bool
    active:bool
    create_at:datetime
    updated_at:datetime

    class Config():
       orm_mode = True

   