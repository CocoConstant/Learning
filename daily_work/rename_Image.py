import os
import sys
import shutil

image_path = sys.argv[1]
image_list = os.listdir(image_path)

os.makedirs('/mnt/c/Users/ouyangkang/Desktop/special_diractory')

for num, image in enumerate(image_list):
    shutil.copy(image_path + image, '/mnt/c/Users/ouyangkang/Desktop/special_diractory' + '/' + str(num + 1) + '.tif')