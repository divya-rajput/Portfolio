from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status 
from starlette import status
from models import Education
from datetime import date
from database import SessionLocal


router = APIRouter(
    prefix='/education',
    tags=['education']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
# user_dependency = Annotated[dict, Depends(get_current_user)]

class EducationRequest(BaseModel):
    degree_name: str = Field(min_length=3)
    college_name: str = Field(min_length=3)
    course_name: str = Field(min_length=3)
    description: str = Field(min_length=3)
    start_date: date 
    end_date: date
    
### Endpoints ###
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_education(db: db_dependency):
    return db.query(Education).all()


@router.get("/{education_id}", status_code=status.HTTP_200_OK)
async def read_skill( db: db_dependency, education_id: int = Path(gt=0)):
    education_model = db.query(Education).filter(Education.id == education_id).first()
    if education_model is not None:
        return education_model
    raise HTTPException(status_code=404, detail='Education not found.')


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo( db: db_dependency,
                      education_request: EducationRequest):
    education_model = Education(**education_request.model_dump())
    db.add(education_model)
    db.commit()


@router.put("/{certificate_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo( db: db_dependency,
                      education_request: EducationRequest,
                      education_id: int = Path(gt=0)):
    education_model = db.query(Education).filter(Education.id == education_id).first()
    if education_model is None:
        raise HTTPException(status_code=404, detail='Education not found.')
    education_model.degree_name = education_request.degree_name
    education_model.college_name = education_request.college_name
    education_model.course_name = education_request.course_name
    education_model.degree_name = education_request.description
    education_model.start_date = education_request.start_date
    education_model.end_date = education_request.end_date
    db.add(education_model)
    db.commit()


@router.delete("/{certificate_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo( db: db_dependency, education_id: int = Path(gt=0)):
    education_model = db.query(Education).first()
    if education_model is None:
        raise HTTPException(status_code=404, detail='Education not found.')
    db.query(Education).filter(Education.id == education_id).delete()
    db.commit()