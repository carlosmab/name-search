import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app.api import app
from app.models.search_result.google_search_result import GoogleSearchResult


class CustomSearchTestCase(unittest.TestCase):
    """
    Testing google se endpint
    """
    
    def setUp(self) -> None:
        self.client: TestClient = TestClient(app)
        
    def tearDown(self) -> None:
        ...
        
    def test_google_search_api_requires_token(self) -> None:
        response = self.client.get("/custom-search/google-cse")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_google_search_service_check_online(self) -> None:
        self.authenticate_client()
        
        response = self.client.get("/custom-search/google-cse/")
        expected_body = {
            "status": "ready",
            "provider": "google",
        }
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_body)
    
    
    def test_google_search_service_retrieve_results(self) -> None:
        self.authenticate_client()
        
        words_to_search = ["hi", "google"]
        payload = {
            "keywords": words_to_search
        }
        
        response = self.client.post("/custom-search/google-cse/", json=payload)
        result = response.json()[0]
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(GoogleSearchResult(**result).dict(), result)
        
    
    def authenticate_client(self) -> None:
        credentials = {
            "username": "user@email.com",
            "password": "password"
        }
        response = self.client.post("auth/get-token", json=credentials)
        token = response.json().get("access_token")
        self.client.headers = {"Authorization": f"Bearer {token}"}