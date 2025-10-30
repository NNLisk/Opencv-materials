import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.figure(figsize=(20,5))
image = cv2.imread('/home/niko/Programming/school/AI/Opencv/opencv_bootcamp_assets_NB3/Apollo_11_Launch.jpg', cv2.IMREAD_COLOR)
imageLine = image.copy()
imageCircle = image.copy()
imageRectangle = image.copy()
imageText = image.copy()

plt.subplot(231);plt.imshow(image[:,:,::-1]);plt.title('space')

cv2.line(imageLine, (200, 100), (400,300), (255,255,0), thickness=5, lineType=cv2.LINE_AA)
cv2.line(imageLine, (400, 250), (400,300), (255,255,0), thickness=5, lineType=cv2.LINE_AA)
cv2.line(imageLine, (350, 300), (400,300), (255,255,0), thickness=5, lineType=cv2.LINE_AA)
plt.subplot(232);plt.imshow(imageLine);plt.title('line')

cv2.circle(imageCircle, (500, 400), 100, (111, 164, 202), thickness=5, lineType=cv2.LINE_AA)
plt.subplot(233);plt.imshow(imageCircle);plt.title('Circle')

cv2.rectangle(imageRectangle, (500,100), (700,600), (184,92,29), thickness=5, lineType=cv2.LINE_AA)
plt.subplot(234);plt.imshow(imageRectangle);plt.title('Rectangle')

cv2.putText(imageText, 'A Rocket', (500, 350), cv2.FONT_HERSHEY_PLAIN, 6, (230, 123, 144), thickness=5, lineType=cv2.LINE_AA)
plt.subplot(235);plt.imshow(imageText);plt.title('A Rocket')
plt.show()