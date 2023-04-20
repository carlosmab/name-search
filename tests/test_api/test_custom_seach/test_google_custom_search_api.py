import unittest
from fastapi.testclient import TestClient
from app.main import app
from app.models.search_result.google_search_result import GoogleSearchResult


class CustomSearchTestCase(unittest.TestCase):
    """
    Testing google se
    """
    
    def setUp(self) -> None:
        self.client: TestClient = TestClient(app)
        
    def tearDown(self) -> None:
        ...
        
    def test_google_search_service_check_online(self) -> None:
        response = self.client.get("/custom-search/google-cse")
        self.assertEqual(response.status_code, 200)
        expected_body = {
            "status": "ready",
            "provider": "google",
        }
        self.assertEqual(response.json(), expected_body)
    
    
    def test_google_search_service_retrieve_results(self) -> None:
        words_to_search = ["hi", "google"]
        payload = {
            "keywords": words_to_search
        }
        response = self.client.post("/custom-search/google-cse/", json=payload)
        self.assertEqual(response.status_code, 200)
        result = response.json()[0]
        self.assertEqual(GoogleSearchResult(**result).dict(), result)