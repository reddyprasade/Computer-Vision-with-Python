# Saving a Video

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# we have To define the codec and create VideoWriter object
# Windows[DIVX]
# Fedora [DIVX,XVID, MJPG, X264, WMV1, WMV2], most used XVID
# MJPG result high size video

fourcc = cv.VideoWriter_fourcc(*'MJPG')
out  = cv.VideoWriter('Viodes/Output.avi',fourcc,20.0,(680,420))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv.flip(frame,-1) # 0 , -1 Revece of X axis

        # write the flipped frame
        out.write(frame)

        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
