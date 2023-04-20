import os
from fastapi import HTTPException, status
import jwt

from dotenv import load_dotenv

load_dotenv()

secret_key = os.environ.get("JWT_SECRET_KEY", "secret_key")
algorithm = os.environ.get("JWT_ALGORITHM", "HS256")


def generate_jwt_token(payload: dict) -> dict:
    """Create a JWT token"""
    
    return {
        "access_token" : jwt.encode(payload, secret_key, algorithm)
    }


def decode_jwt_token(token: str) -> dict:
    try:
        return dict(jwt.decode(token, secret_key, algorithms=[algorithm]))
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired")
    except jwt.exceptions.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token")
