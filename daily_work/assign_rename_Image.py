import os
import shutil
import sys

image_path = sys.argv[1]
image_list = os.listdir(image_path)

segment = 2 # how many pieces of photo
x = int(sys.argv[2]) # please input the x axis nums
y = int(sys.argv[3]) # please input the y axis nums
initial_number = 1

for _ in range(segment):
    os.makedirs(f'/mnt/c/Users/ouyangkang/Desktop/Image_{_}' )


dir_selection = 0 # select directory
count = 0 # swith directory selection
dir_0_count = 1
dir_1_count = 0

for image in image_list:
    
    shutil.copy(image_path + image, '/mnt/c/Users/ouyangkang/Desktop/Image_' + str(dir_selection) + '/' + str(dir_0_count if dir_selection == 0 else dir_1_count) + '.tif')
    
    judgement = initial_number % (x/segment)
    if judgement == 0:
        dir_selection = 1
        count += 1
    
    if count == 2:
        dir_selection = 0
        count =0

    if dir_selection == 0:
        dir_0_count += 1
    else:
        dir_1_count += 1
        
    initial_number += 1