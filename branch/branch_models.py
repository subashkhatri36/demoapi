from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,Date
from app.config.database import Base
from sqlalchemy.orm import relationship


class Branch(Base):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True, index=True)
    branch_name = Column(String)
    branch_address  = Column(String)
    branch_description  = Column(String)
    branch_contact  = Column(String)
    active  = Column(Boolean)
    create_at = Column(Date)
    updated_at = Column(Date)
    company_id = Column(Integer, ForeignKey('companies.id'))    

   