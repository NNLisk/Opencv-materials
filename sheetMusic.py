import cv2
import numpy as np
import matplotlib
#interactive
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# an application example of thresholding. here a sheet music paper is made
# much clearer using thresholding where each pixel is only allowed two values
# 0 and 1, or black and white respectively. here different thresholds are displayed
# clearly the adaptive thresholding provides the best result

path="/home/niko/Programming/school/AI/Opencv/opencv_bootcamp_assets_NB3/"
plt.figure(figsize=(20,5))
img = cv2.imread(f"{path}Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

retval, img_thresh_gbl_1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
retval, img_thresh_gbl_2 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

img_thresh_adp = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

plt.subplot(221); plt.imshow(img, cmap="gray"); plt.title("original")
plt.subplot(222); plt.imshow(img_thresh_gbl_1, cmap="gray"); plt.title("Thresheld\nglobal: 50")
plt.subplot(223); plt.imshow(img_thresh_gbl_2, cmap="gray"); plt.title("Thresheld\nglobal: 130")
plt.subplot(224); plt.imshow(img_thresh_adp, cmap="gray"); plt.title("Thresheld\nAdaptive")

plt.show()