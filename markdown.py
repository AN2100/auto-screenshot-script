import os
import subprocess

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
    filepath = os.path.abspath(filename)

    # Add an image link to the Markdown string
    markdown += f'![{filename}](IMG/{filename})\n\n'

# Write the Markdown string to a file
with open('gallery.md', 'w') as f:
    f.write(markdown)



