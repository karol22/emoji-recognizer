import sys
from os import listdir
from os.path import isfile, join
import os
import random

folder_original = 'normalized_dataset_32x32/'
folders = ['angry', 'happy', 'poo', 'sad', 'surprised']

new_folder = 'normalized_dataset_32x32/'

for fo in folders:
    path = folder_original + fo + '/'
    new_path = new_folder + fo + '/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    size = int(len(onlyfiles)* 0.2)
    test_files = random.sample(onlyfiles, size)
    for f in test_files:
        bashCommand = "mv " + path + f + " ./data/test/" + fo + " ;"
        os.system(bashCommand)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print("here")
    for f in onlyfiles:
        bashCommand = "mv " + path + f + " ./data/train/" + fo + " ;"
        os.system(bashCommand)
