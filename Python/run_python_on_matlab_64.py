
# Run this on matlab!  gnome-terminal  -- python /home/ubuntu/keras/enver/ml512_finetune_loss_12/matlab_test.py
# This is only work when Matlab started from a gnome terminal in Ubuntu!

# https://www.pyimagesearch.com/2014/06/02/opencv-load-image/


#coding=utf-8
from keras.models import load_model
from keras.models import Model
from keras import models
from keras import layers
from keras import optimizers
import cv2
import argparse
import glob
import numpy as np
import sys,os
import matplotlib
import time
import glob
import os, os.path
import re


np.set_printoptions(linewidth=1028)


from keras.models import model_from_json
from keras.models import load_model

json_file = open('/home/ubuntu/keras/enver/dmlh_v2/models/dmlh_v2_64_model.json', 'r')

model = json_file.read()
json_file.close()
model = model_from_json(model)
model.load_weights("/home/ubuntu/keras/enver/dmlh_v2/models/dmlh_v2_64_weights.h5")


from PIL import Image
from keras.preprocessing import image



model = Model(inputs=model.input, outputs=model.get_layer('dense_2').output)





img_1 = "Python/q1.jpg"
img_1 = image.load_img(img_1)
img_1 = image.img_to_array(img_1)
img_1 = img_1.reshape((1,) + img_1.shape)
binary_codes_1 = model.predict(img_1)[0]
binary_codes_1 = binary_codes_1 > 0.5
binary_codes_1 = binary_codes_1.astype(int)





img_2 = "Python/q2.jpg"
img_2 = image.load_img(img_2)
img_2 = image.img_to_array(img_2)
img_2 = img_2.reshape((1,) + img_2.shape)
binary_codes_2 = model.predict(img_2)[0]
binary_codes_2 = binary_codes_2 > 0.5
binary_codes_2 = binary_codes_2.astype(int)



img_3 = "Python/q3.jpg"
img_3 = image.load_img(img_3)
img_3 = image.img_to_array(img_3)
img_3 = img_3.reshape((1,) + img_3.shape)
binary_codes_3 = model.predict(img_3)[0]
binary_codes_3 = binary_codes_3 > 0.5
binary_codes_3 = binary_codes_3.astype(int)


np.savetxt('Python/q1.txt', binary_codes_1,  fmt='%d',  delimiter=',')
np.savetxt('Python/q2.txt', binary_codes_2,  fmt='%d',  delimiter=',')
np.savetxt('Python/q3.txt', binary_codes_3,  fmt='%d',  delimiter=',')












