from typing import Annotated
from fastapi import Body, Depends
from app.routers.custom_api_router import CustomAPIRouter
from app.services.auth.jwt_bearer import JWTBearer
from app.services.data_processing.name_extraction import extract_names_from_text

name_extraction_router = CustomAPIRouter("extract-names")
name_extraction_router.dependencies = [Depends(JWTBearer())]

@name_extraction_router.post("/")
async def extract_names(text: Annotated[str, Body(embed=True)] = "") -> dict:   
    names = extract_names_from_text(text)
    return {"names": names} 