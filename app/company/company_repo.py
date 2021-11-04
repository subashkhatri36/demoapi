from sqlalchemy.orm import Session
from app.company import company_models, company_schemas
from fastapi import HTTPException,status
from datetime import datetime


# Must use UTC datetime.
start_date = datetime.utcnow()

def create(request: company_schemas.Company,db: Session):
    new_company = company_models.Company(user_id=request.user_id, company_name=request.company_name,company_email=request.company_email,company_contact=request.company_contact,company_address=request.company_address,company_logo=request.company_logo,company_pan=request.company_pan,comapny_description=request.comapny_description,owner_citizenship=request.owner_citizenship,branch=request.branch,active=request.active,create_at=start_date,updated_at=start_date)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company