# -*- coding: utf-8 -*-
"""Black and white sketch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DX1sjrsTSzDXSLzyTyh91-tcOfK2qS2b
"""

from google.colab.patches import cv2_imshow

import cv2

"""Inserting a image in this function"""

##insert image path in this single quotation mark
img=cv2.imread('demo-image.jpg')

img

cv2_imshow(img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray

cv2_imshow(gray)

invert=cv2.bitwise_not(gray)

cv2_imshow(invert)

smoothing=cv2.GaussianBlur(invert,(21,21),sigmaX=0,sigmaY=0)

def dodging(x,y):
  return cv2.divide(x,255-y,scale=256)

final=dodging(gray,smoothing)

cv2_imshow(final)

