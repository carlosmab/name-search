import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app.api import app
from app.utilities.auth.jwt_handler import decode_jwt_token


class JWTAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
    def test_if_jwt_token_is_retrieved(self):
        credentials = {
            "username": "user@email.com",
            "password": "password"
        }
        
        response = self.client.post("/auth/get-token/", json=credentials)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.json())
        
        
    def test_401_if_invalid_credentials(self):
        credentials = {
            "username": "user@email.com",
            "password": "password1123"
        }
        
        response = self.client.post("/auth/get-token/", json=credentials)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    
        