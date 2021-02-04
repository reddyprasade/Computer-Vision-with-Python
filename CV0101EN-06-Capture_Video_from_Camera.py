# Capture Video from Camera
"""
Learn to capture from Camera and display it. Live
Learn to read video, display video and save video.
You will learn these functions : cv2.VideoCapture(), cv2.VideoWriter()

"""
import numpy as np
import os
import cv2 as cv
# To capture a video, you need to create a VideoCapture object
cap = cv.VideoCapture(0) # 0 Default Cam and 1 mean Second Cam
while (True):
    """
    Video Consist of Frames by Frames Each for 1 Second we will get 24 Frames == One Image
    """
    ret, frame = cap.read()
    # Now i have Convert Gray
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # Display the Result
    cv.imshow('Frame',gray)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
    
    
