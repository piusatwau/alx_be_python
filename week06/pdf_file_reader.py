import PyPDF2

# Open the PDF file in read-binary mode
with open('Marshall-Ganz-People-Power-and-Change.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    
    # Get the number of pages in the PDF
    num_pages = len(reader.pages)
    print(f"Number of pages: {num_pages}")
    
    # Extract text from the first page
    first_page = reader.pages[10]
    text = first_page.extract_text()
    
    print("Text from the first page:")
    print(text)
