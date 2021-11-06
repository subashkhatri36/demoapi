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


def show(id:int,db:Session):
    dbcompnay = db.query(company_models.Company).filter(company_models.Company.id == id).first()
    if not dbcompnay:
        data={'status':'false','data':f"COmpany with the id {id} is not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=data)
    # userresponse={'email':dbuser.email,'id':dbuser.id,'fullname':dbuser.fullname,'profile':dbuser.profile,'last_login':dbuser.last_login,'is_superuser':dbuser.is_superuser,'is_staff':dbuser.is_staff,'date_joined':dbuser.date_joined,"is_active":new_user.is_active}
    response={'detail':{'status':'true','data': dbcompnay}}
    return response