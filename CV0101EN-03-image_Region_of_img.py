# Image ROI(Region of Images)
import cv2 as cv

img = cv.imread('Photes/messi.jpg')
cv.imshow('Orginal Messi_Football',img)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow('Change Messi_Football',img)



"""
import matplotlib.pyplot as plt
data = plt.imread('Photes/messi.jpg')
plt.imshow(data)
plt.show()
"""
