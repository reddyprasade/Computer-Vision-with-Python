import cv2 as cv
import glob
import os
'''
def rename_image():
    """
Converting Multiple Images name into Commman names
    """
    i = 0
    path = "Photes/tulips/"
    for filename in os.listdir(path):
        my_dest ="img_" + str(i) + ".jpeg"
        my_source = path +filename
        my_dest = path+my_dest
        os.rename(my_source, my_dest)
        i += 1
if __name__ == '__main__':
    rename_image()
'''

# By Using glob
filelist = glob.glob('Photes/tulips/*.jpeg')
print(filelist)

#cv
images = [cv.imread(file) for file in glob.glob("Photes/tulips/*.jpeg")]


# Numpy and cv
import numpy as np

instances = []
for filepath in os.listdir('Photes/tulips/'):
    instances.append(cv.imread('Photes/tulips/img_{0}'.format(filepath),0))
print(type(instances[0]))

