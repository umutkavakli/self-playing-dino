import numpy as np
import pandas as pd
import pyautogui
import keyboard
import time
import cv2

X = 225
Y = 150
W = 625
H = 200

FPS = 10
time_delta = 1./FPS # 10 frames per second

target_data = [] # if user press space button add 1 else 0 
print("[INFO] Gathering data from your play for dataset...")

i = 1

try:
    while True:
        if keyboard.is_pressed('space'):
            target_data.append(1)
        else:
            target_data.append(0)

        screenshot = pyautogui.screenshot() # take screenshot of whole screen
        
        img = np.array(screenshot) # convert to numpy array
        img = img[Y:Y+H, X:X+W] # coordinates of roi
        
        image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # convert RGB to BGR for opencv
        image_path = "images/image" + str(i) + ".jpg" 
        cv2.imwrite(image_path, image)

        i+=1
        time.sleep(time_delta) 

except KeyboardInterrupt:
    pass

df = pd.DataFrame(target_data)
df.to_csv("data/target_data.csv", sep=",")
