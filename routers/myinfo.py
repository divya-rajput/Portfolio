from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status 
from starlette import status

router = APIRouter(
    prefix='/profile',
    tags=['profile']
)

profile_response = {
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

@router.get("/", status_code=status.HTTP_200_OK)
async def get_profile():
    return profile_response
