from sqlalchemy import Column, Integer, String, Date,Boolean
from app.config.database import Base




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

    