import cv2
import numpy as np
import matplotlib
#interactive
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

arr1 = np.array([200,250], dtype=np.uint8).reshape(-1,1)
arr2 = np.array([40,40], dtype=np.uint8).reshape(-1,1)
dd = arr1 + arr2
adcv2 = cv2.add(arr1, arr2)

print(dd, adcv2)

cv2.THRO