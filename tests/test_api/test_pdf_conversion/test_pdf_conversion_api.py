import os
import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app.api import app   


class TestPdfUploadAndConvert(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_pdf_conversion_api_requires_token(self) -> None:
        response = self.client.post("/convert-pdf/text")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_upload_pdf_and_convert(self):
        self.authenticate_client()
        
        sample_pdf_content = b"This is a sample PDF content."
        with open("sample.pdf", "wb") as f:
            f.write(sample_pdf_content)

        with open("sample.pdf", "rb") as f:
            response = self.client.post("/convert-pdf/text", files={"file": ("sample.pdf", f)})

        self.assertEqual(response.status_code, 200)

        expected_text = "This is the text extracted from the PDF."
        self.assertEqual(response.json()["text"], expected_text)
        
        os.remove("sample.pdf")
        

    def authenticate_client(self) -> None:
        credentials = {
            "username": "user@email.com",
            "password": "password"
        }
        response = self.client.post("auth/get-token", json=credentials)
        token = response.json().get("access_token")
        self.client.headers = {"Authorization": f"Bearer {token}"}