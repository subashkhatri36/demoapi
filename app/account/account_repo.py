
from sqlalchemy.orm import Session
from app.account import account_models,account_schemas
from fastapi import HTTPException,status
from .hashing import Hash
from datetime import datetime


# Must use UTC datetime.
start_date = datetime.utcnow()

def create(request: account_schemas.User,db:Session):
    new_user = account_models.User(fullname=request.fullname,email=request.email,password=Hash.bcrypt(request.password),profile=request.profile,last_login=start_date,is_superuser=True,is_staff=True,date_joined=start_date,is_active=True)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    userresponse={'email':new_user.email,'id':new_user.id,'fullname':new_user.fullname,'profile':new_user.profile,'last_login':new_user.last_login,'is_superuser':new_user.is_superuser,'is_staff':new_user.is_staff,'date_joined':new_user.date_joined,"is_active":new_user.is_active}
    response={'detail':{'status':'true','data': userresponse}}
    return response

def show(id:int,db:Session):
    dbuser = db.query(account_models.User).filter(account_models.User.id == id).first()
    if not dbuser:
        data={'status':'false','data':f"User with the id {id} is not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=data)
    userresponse={'email':dbuser.email,'id':dbuser.id,'fullname':dbuser.fullname,'profile':dbuser.profile,'last_login':dbuser.last_login,'is_superuser':dbuser.is_superuser,'is_staff':dbuser.is_staff,'date_joined':dbuser.date_joined,"is_active":new_user.is_active}
    response={'detail':{'status':'true','data': userresponse}}
    return response
