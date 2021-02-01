import cv2 as cv

img1 = cv.imread('Photes/Cat03.jpg')
img2 = cv.imread('Photes/bike.jpg')

print("Shape of Cat",img1.shape)
print("Shape of Bike",img2.shape)

px = img1[100,100]
print(px)
cv.imshow('Pixcle Values',px)

# accessing only blue pixel
blue = img1[100,100,0]
print(blue)

# accessing RED value
img1.item(10,10,2)
cv.imshow('Red',img1)

#  Image Properties
print('image Shape',img1.shape)
print('Image Size',img1.shape)
print("Find the Data Type of image",img1.dtype)




cv.waitKey(0)
cv.destroyAllWindows()
