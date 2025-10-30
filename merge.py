import cv2
import numpy as np
import matplotlib
#interactive
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# here a picture, both RGB and HSV is separated into their 3 separate channels
# r,g,b and h,s,v respectively. and then merged back together into the whole picture
# normally the single channel pictures show as grayscale but they can be illustrated
# better with color mapping channels to their respective red green and blue color maps

path="/home/niko/Programming/school/AI/Opencv/opencv_bootcamp_assets_NB3/"
plt.figure(figsize=(20,5))
img = cv2.imread(f"{path}cornifer.jpg", cv2.IMREAD_COLOR)

imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
b, g, r = cv2.split(imageRGB)
plt.subplot(241);plt.imshow(r, cmap="gray");plt.title("Red")
plt.subplot(242);plt.imshow(g, cmap="gray");plt.title("Green")
plt.subplot(243);plt.imshow(b, cmap="gray");plt.title("Blue")
merged = cv2.merge((b,g,r))
plt.subplot(244);plt.imshow(merged);plt.title("Merged")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imgHSV)
plt.subplot(245);plt.imshow(h, cmap="gray");plt.title("Hue")
plt.subplot(246);plt.imshow(s, cmap="gray");plt.title("Saturation")
plt.subplot(247);plt.imshow(v, cmap="gray");plt.title("Value")
mergedHSV = cv2.merge((h + 30,s,v))
original = cv2.cvtColor(mergedHSV, cv2.COLOR_HSV2RGB)
plt.subplot(248);plt.imshow(original);plt.title("Merged HSV")

plt.tight_layout()
plt.show()

# cv2.imshow("red", r)
# cv2.waitKey(0)
# cv2.imshow("green", g)
# cv2.waitKey(0)
# cv2.imshow("blue", b)
# cv2.waitKey(0)
