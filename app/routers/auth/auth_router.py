from fastapi import Body, HTTPException
from app.models.user import UserCredentials
from app.routers.auth.auth_controller import generate_token_response
from app.routers.custom_api_router import CustomAPIRouter


auth_router = CustomAPIRouter("auth")


@auth_router.post("/get-token")
async def get_token(credentials: UserCredentials = Body(...)) -> dict:
    return generate_token_response(credentials)
    
    