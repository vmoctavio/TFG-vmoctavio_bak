#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:52:00 2019
@author: vmoctavio
"""

from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
# pretty progressbar
from tqdm import tqdm

def brightness_adjustment(img):
    # turn the image into the HSV space
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # creates a random bright
    ratio = .5 + np.random.uniform()
    # convert to int32, so you don't get uint8 overflow
    # multiply the HSV Value channel by the ratio
    # clips the result between 0 and 255
    # convert again to uint8
    hsv[:,:,2] =  np.clip(hsv[:,:,2].astype(np.int32) * ratio, 0, 255).astype(np.uint8)
    # return the image int the BGR color space
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# creates an image generator
# better explanation here https://keras.io/preprocessing/image/
img_generator = ImageDataGenerator(preprocessing_function=brightness_adjustment,
                                   rotation_range=2, width_shift_range=0.01,
                                   height_shift_range=0.01, shear_range=0.02,
                                   zoom_range=0.03, channel_shift_range=4.,
                                   horizontal_flip=True, vertical_flip=True,
                                   fill_mode='nearest')
 
# check here for more details
# https://keras.io/preprocessing/image/#imagedatagenerator-methods
images_path = '/users/⁨vmoctavio⁩/⁨OneDrive - Indra⁩/⁨/⁨____TFG⁩/google-images-deep-learning⁩/'
aug_iter = img_generator.flow_from_directory(images_path,
                                             target_size=(224, 224),
                                             shuffle=True, 
                                             batch_size=1)
# number of images to be generated
n_images = 100

# path where the generated images will be stored
path_out =  '/users/⁨vmoctavio⁩/⁨OneDrive - Indra⁩/⁨/⁨____TFG⁩/google-images-deep-learning⁩/new_path/'

for j,i in tqdm(enumerate(range(n_images)), total=len(range(n_images))):
    img = next(aug_iter)[0].astype(np.uint8)[0]
    cv2.imwrite(path_out + str(i) + '.png', img)

# show a generated sample
#cv2.imshow('image' , next(aug_iter)[0].astype(np.uint8)[0])
