import os
from PIL import ImageGrab
import numpy as np
import time
import shutil
import subprocess
import threading
import sys

# Directory name to be created
new_dir_name = "IMG"

# Parent directory where the new directory will be created
parent_dir = os.getcwd()

# Path of the new directory
new_dir_path = os.path.join(parent_dir, new_dir_name)

# Create the new directory
if os.path.exists(new_dir_path) and os.path.isdir(new_dir_path):
   shutil.rmtree(new_dir_path, ignore_errors=True)

os.mkdir(new_dir_path)

# Initialize the previous screenshot

image_change_factor = float(sys.argv[1])

def take_screen(stop):
    i=1
    prev_screen = None
    while (not stop.is_set()):
            # Capture a new screenshot

        curr_screen = ImageGrab.grab()

            # Convert the screenshot to a numpy array
        curr_array = np.array(curr_screen)

            # Compare the current screenshot to the previous screenshot
        if prev_screen is not None:
            diff = np.sum(np.abs(curr_array - prev_array)) / \
                    (curr_array.size * 255)
            if diff >= image_change_factor:
                    # Save the screenshot
                h = time.strftime("%Y%m%d-%H%M%S")
                print(h)
                curr_screen.save("IMG/"+str(i)+'.png')
                i = i + 1

        # Update the previous screenshot
        prev_screen = curr_screen
        prev_array = curr_array
stop = threading.Event()
screen_thread = threading.Thread(target = take_screen ,args =(stop,))
screen_thread.start()
input("Press Enter to exit the program ... ")
stop.set()
screen_thread.join()
print("exiting program : ")

