# auto-screenshot-script
The purpose of this project is to provide an automated way to take screenshots during online classes or while watching videos and create a gallery of the captured images in a Markdown file. This can be helpful for taking notes and studying the material later.

# Implementation
The project consists of three files - "screenshot.py" ,”markdown.py” and "Notes.sh". The "screenshot.py" script uses the PIL library to capture the current screen and compares it to the previous screen to check for any changes. If the change factor is greater than the specified threshold, the current screen is saved as a PNG file in a new directory named "IMG" created in the current working directory.
Running the bat file will execute

- Make sure all the files are in the same directory executing the bat script for windows and the shell script for the linux system
- Following are the package requirements 
  - numpy
  - shutil
  - subprocess
  - threading
  - PIL 
    - ImageGrab

    


