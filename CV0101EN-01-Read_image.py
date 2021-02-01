import cv2 as cv

# Read the image
img = cv.imread('Photes/Cat03.jpg')

# display the image in New window
cv.imshow('Cat',img)

# Keyword binding Key you weant Press
# 0 mean it is inf
# 1 Mean amount of time it will wait
cv.waitKey(0)
