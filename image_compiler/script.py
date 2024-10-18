import os
import img2pdf

# Specify the directory containing the images
image_directory = "E:/swe/my projects/python/alx_be_python/image_compiler"

# Get a list of PNG files with their full paths
image_paths = [os.path.join(image_directory, i) for i in os.listdir(image_directory) if i.endswith(".png")]

# Convert the images to a PDF and write the output to a file
with open("gallery.pdf", "wb") as file:
    file.write(img2pdf.convert(image_paths))
