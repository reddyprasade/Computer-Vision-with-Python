import cv2
import numpy as np
import os

def frames_to_video(inputpath,outputpath,fps):
   image_array = []
   files = [f for f in os.listdir(inputpath) if isfile(join(inputpath, f))]
   files.sort(key = lambda x: int(x[5:-4]))
   for i in range(len(files)):
       img = cv2.imread(inputpath + files[i])
       size =  (img.shape[1],img.shape[0])
       img = cv2.resize(img,size)
       image_array.append(img)
   fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
   out = cv2.VideoWriter(outputpath,fourcc, fps, size)
   for i in range(len(image_array)):
       out.write(image_array[i])
   out.release()


inputpath = 'folder path'
outpath =  'video file path/video.mp4'
fps = 29
frames_to_video(inputpath,outpath,fps)
