from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
from starlette import status
from models import Certificates
from database import SessionLocal


router = APIRouter(
    prefix='/certificates',
    tags=['certificates']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
# user_dependency = Annotated[dict, Depends(get_current_user)]

class CertificateRequest(BaseModel):
    title: str = Field(min_length=3)
    completedOn: str = Field(min_length=3)
    isActive: bool = Field(alias="isActive")

### Endpoints ###
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_certificates(db: db_dependency):
    return db.query(Certificates).all()


@router.get("/{certificate_id}", status_code=status.HTTP_200_OK)
async def read_skill( db: db_dependency, certificate_id: int = Path(gt=0)):
    education_model = db.query(Certificates).filter(Certificates.id == certificate_id).first()
    if education_model is not None:
        return education_model
    raise HTTPException(status_code=404, detail='Certification not found.')


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo( db: db_dependency,
                      education_request: CertificateRequest):
    education_model = Certificates(**education_request.model_dump())
    db.add(education_model)
    db.commit()


@router.put("/{certificate_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo( db: db_dependency,
                      education_request: CertificateRequest,
                      certificate_id: int = Path(gt=0)):
    education_model = db.query(Certificates).filter(Certificates.id == certificate_id).first()
    if education_model is None:
        raise HTTPException(status_code=404, detail='Certification not found.')
    education_model.title = education_request.title
    education_model.completedOn = education_request.completedOn
    education_model.isActive = education_request.isActive
    db.add(education_model)
    db.commit()


@router.delete("/{certificate_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo( db: db_dependency, certificate_id: int = Path(gt=0)):
    education_model = db.query(Certificates).first()
    if education_model is None:
        raise HTTPException(status_code=404, detail='Certification not found.')
    db.query(Certificates).filter(Certificates.id == certificate_id).delete()
    db.commit()
