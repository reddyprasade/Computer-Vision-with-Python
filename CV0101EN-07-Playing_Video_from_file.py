# Playing Video from file
import numpy as np
import cv2 as cv
"""
cv2.VideoCapture(0): Means first camera or webcam.
cv2.VideoCapture(1):  Means second camera or webcam.
cv2.VideoCapture("file_name.mp4"): Means video file
"""
# Method-1

import cv2

cap = cv2.VideoCapture('vtest.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Method -2

cap = cv.VideoCapture('Viodes/vtest.avi') 
if (cap.isOpened()== False):
    print("Error opening video  file")


while(cap.isOpened()):
    ret, frame = cap.read() 
    if ret == True:
        cv.imshow('Frame', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
cv.destroyAllWindows() 
