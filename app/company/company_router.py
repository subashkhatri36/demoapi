from fastapi import APIRouter,Depends,status
from app.config import database
from sqlalchemy.orm import Session
from app.account import account_schemas
from app.company import company_schemas,company_repo
from app.account import oauth2


router=APIRouter(
    prefix="/company",
    tags=['Company']
)

get_db=database.get_db



@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: company_schemas.Company, db: Session = Depends(get_db),current_user: account_schemas.User = Depends(oauth2.get_current_user)):
    return company_repo.create(request, db)




# @router.post('/', status_code=status.HTTP_201_CREATED,)
# def create(request: company_schema.Company, db: Session = Depends(get_db),current_user: userSchemas.User = Depends(oauth2.get_current_user)):
#     return blog.create(request, db)


# @router.post('/',response_model=compnayScheas.showCompany)
#  def create_company(request:compnaySchemas.company,db: Session=Depends(get_db)):
#      return userrepo.create(request,db)


# @router.get('/{id}')
# def get_user(id:int,db: Session = Depends(get_db)):
#     # return JSONResponse(status_code=status.HTTP_200_OK, content=userrepo.show(id,db))
#     response={'detail':{'status':'true','data': userrepo.show(id,db)}}
#     return response