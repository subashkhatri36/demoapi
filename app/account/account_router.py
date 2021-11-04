from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.config import database
from sqlalchemy.orm import Session
from  app.account import account_repo,account_schemas,account_models
from app.account import token
from app.account.hashing import Hash




router=APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db=database.get_db


@router.post('/create',)
async def create_user(request:account_schemas.User,db: Session=Depends(get_db)):
    return account_repo.create(request,db)


# @router.get('/{id}')
# def get_user(id:int,db: Session = Depends(get_db)):
#     # return JSONResponse(status_code=status.HTTP_200_OK, content=userrepo.show(id,db))
#     response={'detail':{'status':'true','data': account_repo.show(id,db)}}
#     return response



@router.post('/',)
async def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user_info = db.query(account_models.User).filter(account_models.User.email == request.username).first()
    if not user_info:
        data={'status':'false','data':f"Invalid Credentials"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=data)
    if not Hash.verify(user_info.password, request.password):
        data={'status':'false','data':f"Incorrect password"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=data)

    access_token = token.create_access_token(data={"sub": user_info.email})
    userresponse={'email':user_info.email,'id':user_info.id,'fullname':user_info.fullname,'profile':user_info.profile,'last_login':user_info.last_login,'is_superuser':user_info.is_superuser,'is_staff':user_info.is_staff,'date_joined':user_info.date_joined}
    data={"access_token": access_token, "token_type": "bearer","user":userresponse}
    response={'detail':{'status':'true','data': data}}
    return response


# @router.get("/logout")
# async def logout(request: Request, response: Response, current_user: User = Depends(get_current_active_user)):
#     # Also tried following two comment lines
#     # response.set_cookie(key="access_token", value="", max_age=1)
#     # response.delete_cookie("access_token", domain="localhost")
#     response = templates.TemplateResponse("login.html", {"request": request, "title": "Login", "current_user": AnonymousUser()})
#     response.delete_cookie("access_token")
#     return response


@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("Authorization", domain="dealerdeal.herokuapp.com")
    data={'detail':{'status':'true','data': response}}
    return data