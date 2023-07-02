import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from classifier import Classifier

TRAINING_DIR = './images/train'
TEST_DIR = './images/test'

classifier = Classifier()

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    # width_shift_range=0.2,
    # height_shift_range=0.2,
    # zoom_range=0.2,
    # shear_range=0.2,
    # fill_mode='nearest'
)

test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
)

train_flow = classifier.get_flow(
    TRAINING_DIR,
    train_datagen
)

test_flow = classifier.get_flow(
    TEST_DIR,
    test_datagen
)

callbacks = [
   tf.keras.callbacks.ModelCheckpoint(
       './checkpoints4/checkpoint-{epoch:02d}-{val_loss:.2f}.h5', 
        monitor='val_loss', 
        save_best_only=True, 
        save_weights_only=True, 
        mode='min'
   )
]

model = classifier.build_model()
model.compile(
    optimizer='adam', 
    loss='categorical_crossentropy', 
    metrics=['accuracy']
)

history = model.fit(
    train_flow,
    epochs=25,
    validation_data=test_flow,
    callbacks=callbacks,
    workers=0
)