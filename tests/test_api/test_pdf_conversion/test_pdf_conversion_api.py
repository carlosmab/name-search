import os
import unittest
from fastapi.testclient import TestClient
from fastapi import status
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from app.api import app   


class PdfConversionAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.create_sample_pdf("sample.pdf")
        
    def tearDown(self):
        os.remove("sample.pdf")

    def test_pdf_conversion_api_requires_token(self) -> None:
        response = self.client.post("/convert-pdf/text")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_upload_pdf_and_convert(self):
        self.authenticate_client()

        with open("sample.pdf", "rb") as f:
            response = self.client.post("/convert-pdf/text", files={"file": ("sample.pdf", f)})

        self.assertEqual(response.status_code, 200)

        expected_text = "This is the text extracted from the PDF.\n"
        self.assertEqual(response.json()["text"], expected_text)
        
        
    def authenticate_client(self) -> None:
        credentials = {
            "username": "user@email.com",
            "password": "password"
        }
        response = self.client.post("auth/get-token", json=credentials)
        token = response.json().get("access_token")
        self.client.headers = {"Authorization": f"Bearer {token}"}
        
        
    def create_sample_pdf(self, file_path):
        c = canvas.Canvas(file_path, pagesize=letter)
        c.drawString(100, 700, "This is the text extracted from the PDF.")
        c.save()