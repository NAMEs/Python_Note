import cv2 
import numpy

img = cv2.imread("839462.png", cv2.IMREAD_UNCHANGED)

cv2.namedWindow('Image',cv2.WINDOW_AUTOSIZE)

cv2.imshow('Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()



