import cv2
import numpy as np
import matplotlib
#interactive
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#this program displays examples of bitwise operations with opencv
#this means two pictures are combined comparing each bit with for example
# AND, OR, XOR bitwise comparisons

# example
# bits 1, 1
# AND  1
# OR   1
# XOR  0

path="/home/niko/Programming/school/AI/Opencv/opencv_bootcamp_assets_NB3/"
plt.figure(figsize=(20,5))
imgr = cv2.imread(f"{path}rectangle.jpg", cv2.IMREAD_GRAYSCALE)
imgc = cv2.imread(f"{path}circle.jpg", cv2.IMREAD_GRAYSCALE)

plt.subplot(151); plt.imshow(imgr, cmap="gray");plt.title("rectangle")
plt.subplot(152); plt.imshow(imgc, cmap="gray");plt.title("circle")

resultand = cv2.bitwise_and(imgr, imgc, mask=None)
resultor = cv2.bitwise_or(imgr, imgc, mask=None)
resultxor= cv2.bitwise_xor(imgr, imgc, mask=None)


plt.subplot(153);plt.imshow(resultand, cmap="gray");plt.title("bitwise and")
plt.subplot(154);plt.imshow(resultor, cmap="gray");plt.title("bitwise or")
plt.subplot(155);plt.imshow(resultxor, cmap="gray");plt.title("bitwise xor")

plt.show()