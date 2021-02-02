# Arithmetic Operations on Images
"""
* Learn several arithmetic operations on images like addition, subtraction, bitwise operations etc.
* You will learn these functions : cv2.add(), cv2.addWeighted() etc.
"""
import cv2 as cv
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print("Computer vision Addation",cv.add(x,y))  # 250+10 = 260 ==> 255 
print("Python Addation",x+y) # 250+10= 260 % 256 =4




# Image Blending
img1 = cv.imread('Photes/ml.jpg')
img2 = cv.imread('Photes/opencv-logo-white.png')

print(img1.shape)
print(img2.shape)

img2_resized = cv.resize(img2, (img1.shape[1], img1.shape[0]))
dst = cv.addWeighted(img1, 0.7, img2_resized, 0.3, 0)

cv.imshow('dst',dst)


# Bitwise Operations

img1 = cv.imread('Photes/messi.jpg')
img2 = cv.imread('Photes/opencv-logo-white.png')

# Now I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

# now i want to Create a mask of logo and create it's inverse mask
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# now Black out the area of Logo ROI
img1_bg =cv.bitwise_and(roi,roi,mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# We ahave to Put logo in ROI and Modify main Image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows,0:cols] =dst
cv.imshow('DST',dst)
cv.imshow('Res',img1)
cv.waitKey(0)
cv.destroyAllWindows()


