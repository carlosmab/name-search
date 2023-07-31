import PyPDF2


# NOTE: This method was generated using "ChatGPT 3" it could lead to 
# potential security risks or be outdated. 
# Carefully review and validate all inputs and outputs
def convert_pdf_to_text(filename: str) -> str:
    """
    
    """
    with open(filename, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)
        text = ""
        for page in range(pdf.numPages):
            text += pdf.getPage(page).extractText()
    return text