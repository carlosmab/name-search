import os
from fastapi import Depends, UploadFile, File
from app.routers.custom_api_router import CustomAPIRouter
from app.services.auth.jwt_bearer import JWTBearer
from app.services.pdf_conversion.convert_pdf_to_text import convert_pdf_to_text

pdf_conversion_router = CustomAPIRouter("convert-pdf")
pdf_conversion_router.dependencies = [Depends(JWTBearer())]

# Endpoint to receive and process the uploaded PDF file
@pdf_conversion_router.post("/text/")
async def upload_pdf_file(file: UploadFile = File(...)):

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    file_path = os.path.join("uploads", file.filename or "")
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = convert_pdf_to_text(file_path)

    return {"text": text}