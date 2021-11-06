from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,Date
from app.config.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)
    profile=Column(String)
    last_login=Column(Date)
    is_superuser=Column(Boolean)
    is_staff=Column(Boolean)
    is_active=Column(Boolean)
    date_joined=Column(Date)

    usercompany=relationship('Company', back_populates="userlist")

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    company_email = Column(String)
    company_contact = Column(String)
    company_address=Column(String)
    company_logo = Column(String)
    company_pan = Column(String)
    comapny_description=Column(String)
    owner_citizenship=Column(String)    
    branch=Column(Boolean)
    active=Column(Boolean)
    create_at=Column(Date)
    updated_at=Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    userlist=relationship("User", back_populates="usercompany")

