import cv2
import numpy as np
import matplotlib
#interactive
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# this program displays examples of image manipulation such as cropping and scaling


imageBGR = cv2.imread('/home/niko/Programming/school/AI/Opencv/opencv_bootcamp_assets_NB3/thepenitentone.jpg', cv2.IMREAD_COLOR)
imageRGB = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20,4))

plt.subplot(241);plt.imshow(imageRGB);plt.title("Penitent")

cropped = imageRGB[200:600, 400:1000]
plt.subplot(242);plt.imshow(cropped);plt.title("Cropped\nPenitent")

resized = cv2.resize(cropped, None, fx=2, fy=2)
plt.subplot(243);plt.imshow(resized);plt.title("Bigger\nCropped\nPenitent")

w = 100
h = 200
dim = (w, h)

newResized = cv2.resize(cropped, dsize=dim, interpolation=cv2.INTER_AREA)
plt.subplot(244);plt.imshow(newResized);plt.title("odd\nCropped\nPenitent")

dw = 100
aspectRatio = dw / cropped.shape[1]
dh = int(cropped.shape[0] * aspectRatio)
dimm = (dw, dh)

newnewresized = cv2.resize(cropped, dsize=dimm, interpolation=cv2.INTER_AREA)
plt.subplot(141);plt.imshow(newnewresized);plt.title("Even\nOdder")

plt.subplots_adjust(wspace=1.0, hspace=1.0, left=0.05, right=0.95, top=0.95, bottom=0.05)
plt.tight_layout(pad=2.0, w_pad=3.0, h_pad=3.0)
plt.show()

#individual pixels
print(imageBGR[0,0])
print(imageBGR[433, 999])