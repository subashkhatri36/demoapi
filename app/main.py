# main.py
from fastapi import FastAPI
from app.config.database import engine
from app.account import account_models,account_router
from app.company import company_models,company_router



app = FastAPI()

account_models.Base.metadata.create_all(engine)
company_models.Base.metadata.create_all(engine)

app.include_router(account_router.router)
app.include_router(company_router.router)




@app.get("/")
def index():
    return {"message":"Please use relaible directory to work on database. Thank you."}