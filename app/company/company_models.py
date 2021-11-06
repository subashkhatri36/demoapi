from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,Date
from app.config.database import Base


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    company_email = Column(String)
    company_contact = Column(String)
    company_address=Column(String)
    company_logo = Column(String)
    company_pan = Column(String)
    comapany_description=Column(String)
    owner_citizenship=Column(String)    
    branch=Column(Boolean)
    active=Column(Boolean)
    create_at=Column(Date)
    updated_at=Column(Date)
    user_id = Column(Integer)
    