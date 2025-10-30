import cv2
import numpy as np
import matplotlib
#interactive
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# image thresholding, more in ./sheetMusic.py

path="/home/niko/Programming/school/AI/Opencv/opencv_bootcamp_assets_NB3/"
plt.figure(figsize=(20,5))
img = cv2.imread(f"{path}building-windows.jpg", cv2.IMREAD_GRAYSCALE)

retval, treshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
plt.subplot(121);plt.imshow(img,cmap='gray');plt.title('Image')
plt.subplot(122);plt.imshow(treshold, cmap='gray');plt.title('threshold')

plt.show()