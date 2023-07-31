import PyPDF2


# NOTE: This method was generated using "ChatGPT 3" it could lead to 
# potential security risks or be outdated. 
# Carefully review and validate all inputs and outputs
def convert_pdf_to_text(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text