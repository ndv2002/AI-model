import sys
import json
import requests
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import cv2
import time
import os


# loading the stored model from file
IMG_SIZE=64
absolute_path = os.path.join(os.getcwd(), 'Model','Fire.h5')
model=load_model(absolute_path)
# image = cv2.imread(r'D:\Study\doancn\testdataset\fire\frame0.jpg')
absolute_path = os.path.join(os.getcwd(), 'fire.jpg')
image = cv2.imread(absolute_path)

image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
# print(image.shape)
fire_prob = model.predict(image)[0][0] * 100
print(fire_prob)
sys.stdout.flush()


