import os
import sys

image_path = sys.argv[1]
image = os.listdir(image_path)

n = 0 # set the initial figure
for i in image:
    n += 1
    os.rename(image_path+i, image_path + str(n) + '.' + 'tif')