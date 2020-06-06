import cv2
import sys
import numpy
from os import listdir
from os.path import isfile, join

folder_original = 'original_dataset/'
folders = ['angry', 'happy', 'poo', 'sad', 'surprised']

new_folder = 'normalized_dataset_32x32/'

for fo in folders:
    print("Starting with folder " + fo)
    path = folder_original + fo + '/'
    new_path = new_folder + fo + '/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for img_name in onlyfiles:
        im_gray = cv2.imread(path + img_name, cv2.IMREAD_GRAYSCALE) 

        min_x = 2000
        max_x = -1
        min_y = 2000
        max_y = -1
        for i in range(len(im_gray)):
            for j in range(len(im_gray[0])):
                if(im_gray[i][j] == 0):
                    if( i < min_x):
                        min_x = i
                    if( j < min_y):
                        min_y = j
                    if( i > max_x):
                        max_x = i
                    if( j > max_y):
                        max_y = j  

        crop_img = im_gray[min_x:max_x, min_y:max_y]
        resized = cv2.resize(crop_img,(48,48), interpolation=cv2.INTER_AREA)
        for i in range(len(resized)):
            for j in range(len(resized[0])):
                if(resized[i][j] != 255):
                    resized[i][j] = 0
        cv2.imwrite(new_path + img_name, resized)
