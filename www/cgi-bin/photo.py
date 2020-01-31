
import cv2

y = cv2.VideoCapture(0)

ret,photo = y.read()

cv2.imwrite("/root/Desktop/df.png",photo)

y.release()

