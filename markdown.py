import os
import subprocess
import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
arg1 = "screenshot"
# Path to the directory to list
directory_path = os.getcwd()

# Get the list of files in the directory
file_list = os.listdir(directory_path+"/IMG")


# List of image filenames
image_files = []
img = []

# Print the list of files
for filename in file_list:
    image_files.append(filename)
for i in image_files:
    img.append(i[:-4])

for i in range(0, len(img)) :
    img[i] = int(img[i])
img.sort()
for i in range(0, len(img)) :
    img[i] = str(img[i])+'.png'
# print(img)
#image_files.sort()

# Markdown file header
markdown = '# My Image Gallery\n\n'

# Add an image link for each image file
for filename in img:
    # Get the image file path
    
    filepath = os.path.join(directory_path+"\IMG", filename)
    
    # filepath = os.path.abspath(filename)
    
    print(filepath)
    image = Image.open(filepath)

    # Use pytesseract to extract text
    
    text = pytesseract.image_to_string(image)
        
        
    # Encode the text to bytes, ignoring non-unicode characters, then decode back to string
    text = text.encode("ascii", "ignore").decode()
    # Add an image link to the Markdown string
    markdown += f'![{filename}](IMG/{filename})\n\n{text}\n\n'

# Write the Markdown string to a file
with open('gallery.md', 'w') as f:
    f.write(markdown)

# Specify the names of your input and output files
markdown_file = 'gallery.md'
html_file = 'output.html'

# Call Pandoc to convert the Markdown file to a PDF
subprocess.run(['pandoc', markdown_file, '-o', html_file])


