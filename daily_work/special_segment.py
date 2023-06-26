import os
import sys
import shutil

image_path = sys.argv[1]
image_list = os.listdir(image_path)
segment_dir = int(sys.argv[2])

for _ in range(segment_dir):
    os.makedirs('/mnt/c/Users/ouyangkang/Desktop/Image_' + str(_))

segment_num = sys.argv[3]
segment_end = sys.argv[4]

first = 0
second = 0
third = 0

for num, image in enumerate(image_list):
    if num + 1 <= segment_num:
        first += 1
        shutil.copy(image_path + image, '/mnt/c/Users/ouyangkang/Desktop/Image_0' + '/' + str(first) + '.tif')
    if num + 1 > segment_num and num + 1 <= segment_end:
        second += 1
        shutil.copy(image_path + image, '/mnt/c/Users/ouyangkang/Desktop/Image_1' + '/' + str(first) + '.tif')
    if num + 1 > segment_end:
        third += 1
        judge = (num + 1) - (third*)