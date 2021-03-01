import numpy as np
import matplotlib.pyplot as plt
import cv2

vidcap  = cv2.VideoCapture('SampleVideo_1280x720_1mb.mp4')
success,image = vidcap.read()
count = 0

while success:
    cv2.imwrite("frame%d.jpg" % count,image)  # Each and every frame save it JPGE
    success,image =vidcap.read()
    print("Read New Frame:" , success)
    count+=1
