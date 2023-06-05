import fitz
import re
import os
def pdf_text():
    # File upload
    pdf_file = ("Result/output.pdf")
    if pdf_file is not None:
        text = extract_text(pdf_file)
        os.remove(pdf_file)
    return text

def extract_text(pdf_file):
    with fitz.open(pdf_file) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        # Replace all numeric values with an empty string
        text = re.sub(r'\d+', '', text)
        return text

