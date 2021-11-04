from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,Date
from app.config.database import Base
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
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
    userlist=relationship("User", back_populates="usercompany")