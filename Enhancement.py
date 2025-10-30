import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# this program displays examples of picture enhancement methods like
# increasing/decreasing contrast and brightness of an image

# it also displays an issue and a fix to the overflow of multiplying
# or increasing contrast of a picture so that some pixels exceed the 
# rgb 255 value limit

path="/home/niko/Programming/school/AI/Opencv/opencv_bootcamp_assets_NB3/"
plt.figure(figsize=(20,5))
imgCLIFFBGR = cv2.imread(f"{path}New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
imgCLIFFRGB = cv2.cvtColor(imgCLIFFBGR, cv2.COLOR_BGR2RGB)

matrix = np.ones(imgCLIFFRGB.shape, dtype='uint8') * 100
cliffBrighter = cv2.add(imgCLIFFRGB, matrix)
cliffDarker = cv2.subtract(imgCLIFFRGB, matrix)
plt.subplot(331);plt.imshow(cliffBrighter);plt.title('brighter')
plt.subplot(332);plt.imshow(imgCLIFFRGB);plt.title('coast')
plt.subplot(333);plt.imshow(cliffDarker);plt.title('darker')

matrix1 = np.ones(imgCLIFFRGB.shape) * 0.8
matrix2 = np.ones(imgCLIFFRGB.shape) * 1.2
imgLWRCONTR = np.uint8(cv2.multiply(np.float64(imgCLIFFRGB), matrix1))
imgHGRCONTR = np.uint8(cv2.multiply(np.float64(imgCLIFFRGB), matrix2))
plt.subplot(334);plt.imshow(imgLWRCONTR);plt.title('Low Contrast')
plt.subplot(335);plt.imshow(imgCLIFFRGB);plt.title('Normal Contrast')
plt.subplot(336);plt.imshow(imgHGRCONTR);plt.title('High Contrast\n(overflow)')


matrix1 = np.ones(imgCLIFFRGB.shape) * 0.3
matrix2 = np.ones(imgCLIFFRGB.shape) * 1.7
imgLWRCONTRfix = np.uint8(cv2.multiply(np.float64(imgCLIFFRGB), matrix1))
imgHGRCONTRfix = np.uint8(np.clip(cv2.multiply(np.float64(imgCLIFFRGB), matrix2), 8, 255))
plt.subplot(337);plt.imshow(imgLWRCONTRfix);plt.title('Low Contrast')
plt.subplot(338);plt.imshow(imgCLIFFRGB);plt.title('Normal Contrast')
plt.subplot(339);plt.imshow(imgHGRCONTRfix);plt.title('High Contrast')

plt.show()