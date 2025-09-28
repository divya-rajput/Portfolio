from fastapi import FastAPI, Request, status
from models import Base
from database import engine 
from routers import skills,certificates,education,myinfo
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from models import Base
from database import engine  # assuming you have an engine defined

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(skills.router)
app.include_router(certificates.router)
app.include_router(education.router)
app.include_router(myinfo.router)
