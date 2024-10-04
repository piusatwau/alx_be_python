import os

# Specify the path to your PDF file
pdf_file = "Marshall-Ganz-People-Power-and-Change.pdf"

# Check if the file exists and open it
if os.path.exists(pdf_file):
    os.startfile(pdf_file)  # On Windows
    # On macOS or Linux, you would use:
    # os.system(f"open {pdf_file}")  # macOS
    # os.system(f"xdg-open {pdf_file}")  # Linux
else:
    print(f"{pdf_file} not found.")
