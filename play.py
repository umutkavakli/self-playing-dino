import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import mss
import cv2
import time
import keyboard
import numpy as np
import tensorflow as tf

def up():
    keyboard.release(keyboard.KEY_DOWN)
    keyboard.press(keyboard.KEY_UP)
    print('UP\n')

def down():
    keyboard.release(keyboard.KEY_UP)
    keyboard.press(keyboard.KEY_DOWN)
    print('DOWN\n')

def ground():
    keyboard.release(keyboard.KEY_DOWN)
    keyboard.release(keyboard.KEY_UP)
    print('GROUND\n')

# coordinates of ROI
X = 320
Y = 210
WIDTH = 100
HEIGHT = 100
CHANNELS = 1

# time delay for keyboard 
DELAY = 0.000000001
CLASSES = {0: down, 1: ground, 2: up}
ROI = {'top': Y, 'left': X, 'width': WIDTH, 'height': HEIGHT}

def main():
    monitor = mss.mss()

    with open('model.json', 'r') as json_file:
        json_model = json_file.read()

    model = tf.keras.models.model_from_json(json_model)
    model.load_weights('dino_weights.h5')
    print('Model loaded...\n')

    while(1):
        # grab the image
        ss = np.array(monitor.grab(ROI))
        ss = cv2.cvtColor(ss, cv2.COLOR_BGRA2GRAY)
        
        # reshape and normalize
        image = ss.reshape(1, 100, 100).astype('float32')
        image /= 255

        # model prediction
        y_pred = model.predict(image, verbose=0)
        y_pred = np.argmax(y_pred)
        
        # calling the proper movement -> up, down, nothing
        CLASSES[y_pred]()
        time.sleep(DELAY)

if __name__ == '__main__':
    main()
