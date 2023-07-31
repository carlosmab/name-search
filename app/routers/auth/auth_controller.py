from fastapi import HTTPException
from app.models.user import UserCredentials
from app.services.auth.jwt_handler import generate_jwt_token



credentials_test = {
    "username": "user@email.com",
    "password": "password"
}

def validate_credentials(credentials: UserCredentials) -> bool:
    return credentials.dict() == credentials_test


def generate_token_response(credentials: UserCredentials) -> dict: 
    if not validate_credentials(credentials):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return generate_jwt_token(credentials.dict(),)
    
    

