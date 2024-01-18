'''
This python script is designed to rename the image and assign the image to diractory
example: "python rename_Image.py diractory_path 5 10"
The 5 means breakpoint and 10 means the end of one row
author: ouyangkang
'''

import os
import sys
import shutil

image_path = sys.argv[1]
image_list = os.listdir(image_path)

segment_dir = 2
for _ in range(segment_dir):
    os.makedirs('/mnt/c/Users/ouyangkang/Desktop/Image_' + str(_))

segment_start = int(sys.argv[2])
segment_end = int(sys.argv[3])

first = 0
second = 0

for num, image in enumerate(image_list):
    if num % segment_end <= (segment_start - 1):
        first += 1
        shutil.copy(image_path + image, '/mnt/c/Users/ouyangkang/Desktop/Image_0' + '/' + str(first) + '.tif')
    else:
        second += 1
        shutil.copy(image_path + image, '/mnt/c/Users/ouyangkang/Desktop/Image_1' + '/' + str(second) + '.tif')
