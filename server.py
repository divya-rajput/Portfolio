from fastapi import FastAPI, Request, status
from models import Base
from database import engine 
from routers import skills,certificates,education,myinfo
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from models import Base
import logging
from database import engine  # assuming you have an engine defined

Base.metadata.create_all(bind=engine)

server = FastAPI()

@server.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        logging.debug("Connected to postgres")
        return {"status": "Healthy", "database": "Connected"}
    except Exception as e:
        logging.error(str(e))
        return {"status": "Unhealthy", "database": "Disconnected"}



server.include_router(myinfo.router)
server.include_router(skills.router)
server.include_router(certificates.router)
server.include_router(education.router)
