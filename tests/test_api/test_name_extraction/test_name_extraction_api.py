import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app.api import app 

class NameExtractionAPITestCase(unittest.TestCase):
    """
        Test name extraction endpoint
    """
    def setUp(self):
        self.client = TestClient(app)


    def test_name_extraction_api_requires_token(self) -> None:
        response = self.client.post("/extract-names/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_extract_names_valid_input(self):
        self.authenticate_client()
        
        text = "John Doe and Jane Smith are working together since the met."
        
        response = self.client.post("/extract-names/", json={"text": text})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(response.json()["names"], ["John Doe", "Jane Smith"])


    def test_extract_names_empty_input(self):
        self.authenticate_client()
        
        text = ""
        response = self.client.post("/extract-names/", json={"text": text})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(response.json()["names"], [])


    def test_extract_names_no_names_in_text(self):
        self.authenticate_client()
        
        text = "The quick brown fox jumps over the lazy dog."
        
        response = self.client.post("/extract-names/", json={"text": text})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(response.json()["names"], [])
    
    
    def authenticate_client(self) -> None:
        credentials = {
            "username": "user@email.com",
            "password": "password"
        }
        response = self.client.post("auth/get-token", json=credentials)
        token = response.json().get("access_token")
        self.client.headers = {"Authorization": f"Bearer {token}"}