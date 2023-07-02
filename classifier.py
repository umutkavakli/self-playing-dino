import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input


class Classifier:
    def __init__(self, shape):
        self.shape = shape

    def build_model(self):
        inputs = Input(self.shape)

        x = Conv2D(32, (3, 3), activation='relu') (inputs)
        x = MaxPooling2D(pool_size=(2, 2), strides=2) (x)

        x = Conv2D(32, (3, 3), activation='relu') (x)
        x = MaxPooling2D(pool_size=(2, 2), strides=2) (x)        

        x = Conv2D(64, (3, 3), activation='relu') (x)
        x = MaxPooling2D(pool_size=(2, 2), strides=2) (x)

        x = Flatten() (x)
        x = Dense(128, activation='relu') (x)
        x = Dropout(0.5) (x)
        outputs = Dense(3, activation='softmax') (x)

        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        return model
    
    def get_flow(self, data_path, generator, target_size=(100, 100), batch_size=8):
        data_flow = generator.flow_from_directory(
            data_path,
            target_size = target_size,
            color_mode='grayscale',
            batch_size=batch_size,
            class_mode='categorical'
        )

        return data_flow
