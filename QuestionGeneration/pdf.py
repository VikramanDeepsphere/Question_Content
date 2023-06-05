import streamlit as st
import PyPDF2
import base64



def header_footer_cuter(uploaded_file):
    pdf_reader = PyPDF2.PdfReader (uploaded_file)
    pdf_writer = PyPDF2.PdfWriter ()
    # Remove header and footer from each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num] 
        page_media_box = page.mediabox

        # Remove header by adjusting the media box
        header_height = 40
        page_media_box.upper_right = (page_media_box.right, page_media_box.top - header_height)

        # Remove footer by adjusting the media box
        footer_height = 80
        page_media_box.lower_left = (page_media_box.left, page_media_box.bottom + footer_height)

        # Add modified page to output PDF
        pdf_writer.add_page(page)
        

        # Save output PDF file
        output_file = "Result/output.pdf"
        with open(output_file, "wb") as f:
            pdf_writer.write(f)
 