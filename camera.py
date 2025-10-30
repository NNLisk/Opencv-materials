import cv2
import sys

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

winName = "Camera view"

cv2.namedWindow(winName, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:
    has_frame, frame  = source.read()
    if not has_frame:
        break
    cv2.imshow(winName, frame)

source.release()
cv2.destroyWindow(winName)

