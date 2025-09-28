from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
from starlette import status
from models import Skills
from database import SessionLocal


router = APIRouter(
    prefix='/skills',
    tags=['skills']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
# user_dependency = Annotated[dict, Depends(get_current_user)]

class SkillRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    level: int = Field(gt=0, lt=6)


### Endpoints ###
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_skills(db: db_dependency):
    return db.query(Skills).all()


@router.get("/{skill_id}", status_code=status.HTTP_200_OK)
async def read_skill( db: db_dependency, skill_id: int = Path(gt=0)):
    skill_model = db.query(Skills).filter(Skills.id == skill_id).first()
    if skill_model is not None:
        return skill_model
    raise HTTPException(status_code=404, detail='skill not found.')


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo( db: db_dependency,
                      skill_request: SkillRequest):
    skill_model = Skills(**skill_request.model_dump())
    db.add(skill_model)
    db.commit()


@router.put("/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo( db: db_dependency,
                      skill_request: SkillRequest,
                      skill_id: int = Path(gt=0)):
    skill_model = db.query(Skills).filter(Skills.id == skill_id).first()
    if skill_model is None:
        raise HTTPException(status_code=404, detail='Skill not found.')
    skill_model.title = skill_request.title
    skill_model.description = skill_request.description
    skill_model.level = skill_request.level
    db.add(skill_model)
    db.commit()


@router.delete("/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo( db: db_dependency, skill_id: int = Path(gt=0)):
    skill_model = db.query(Skills).first()
    if skill_model is None:
        raise HTTPException(status_code=404, detail='Skill not found.')
    db.query(Skills).filter(Skills.id == skill_id).delete()
    db.commit()












