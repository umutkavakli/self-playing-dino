import cv2
import time
import pathlib
import keyboard
import pyautogui
import numpy as np

# coordinates of region of interest
X = 320
Y = 210
W = 100
H = 100

FPS = 100
wait_time = 1./FPS # 100 frames per second

pathlib.Path('./source/UP').mkdir(parents=True, exist_ok=True)
pathlib.Path('./source/DOWN').mkdir(parents=True, exist_ok=True)
pathlib.Path('./source/GROUND').mkdir(parents=True, exist_ok=True)
#erase_old_images()

# create dataset directories if not exists

status = 'GROUND' 
print("[INFO] Gathering data from your play for dataset...")

i = 0

try:
    while True:
        if keyboard.is_pressed('up'):
            status = 'UP'
        elif keyboard.is_pressed('down'):
            status = 'DOWN'
        else:
            status = 'GROUND'

        screenshot = pyautogui.screenshot() # take screenshot of whole screen
        
        img = np.array(screenshot) # convert to numpy array
        img = img[Y:Y+H, X:X+W] # coordinates of roi
        
        image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # convert RGB to BGR for opencv
        image_path = f'source/{status}/image-{i:05d}.jpg'
 
        cv2.imwrite(image_path, image)

        i+=1
        time.sleep(wait_time) 

except KeyboardInterrupt:
    print('Keyboard interrupted.')

