import PyPDF2

def search_keyword_in_pdf(pdf_path, keyword):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Get the number of pages in the PDF
        num_pages = len(reader.pages)
        print(f"Number of pages: {num_pages}")
        
        # Search for the keyword in each page
        occurrences = {}
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            
            if text:
                # Count the keyword occurrences on this page
                keyword_count = text.lower().count(keyword.lower())
                
                if keyword_count > 0:
                    occurrences[page_num + 1] = keyword_count
        
        return occurrences

# Example usage:
pdf_path = 'Marshall-Ganz-People-Power-and-Change.pdf'
keyword = 'people'

# Search for the keyword in the PDF
occurrences = search_keyword_in_pdf(pdf_path, keyword)

if occurrences:
    print(f"The keyword '{keyword}' was found on the following pages:")
    for page, count in occurrences.items():
        print(f"Page {page}: {count} occurrence(s)")
else:
    print(f"The keyword '{keyword}' was not found in the document.")
