from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status 
from starlette import status

router = APIRouter(
    prefix='/profile',
    tags=['profile']
)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency = Annotated[Session, Depends(get_db)]
# # user_dependency = Annotated[dict, Depends(get_current_user)]

# class PersonalRequest(BaseModel):
#     degree_name: str = Field(min_length=3)
#     college_name: str = Field(min_length=3)
#     course_name: str = Field(min_length=3)
#     description: str = Field(min_length=3)
#     start_date: date 
#     end_date: date
    
# ### Endpoints ###
# @router.get("/", status_code=status.HTTP_200_OK)
# async def read_all_education(db: db_dependency):
#     return db.query(Education).all()


# @router.get("/", status_code=status.HTTP_200_OK)
# async def read_skill( db: db_dependency, education_id: int = Path(gt=0)):
#     education_model = db.query(Education).filter(Education.id == education_id).first()
#     if education_model is not None:
#         return education_model
#     raise HTTPException(status_code=404, detail='Education not found.')

@router.get("/", status_code=status.HTTP_200_OK)
async def getmyinfo():
    # Hardcoded response
    return {
        "email": "divya@example.com",
        "first_name": "Divya",
        "last_name": "Rajput",
        "designation": "Software Engineer",
        "description": "Passionate backend developer with a love for FastAPI.",
        "phone_number": "+1-778-858-4813",
        "location": "Calgary, AB, Canada",
        "socials": {
            "github": "https://github.com/divya-rajput",
            "linkedin": "https://linkedin.com/in/divya-rajput",
            "instagram": "https://instagram.com/realdivyarajput"
        }
    }
