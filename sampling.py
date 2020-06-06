import sys
from os import listdir
from os.path import isfile, join
import os
import random

folder_original = 'normalized_dataset_32x32/'
folders = ['angry']

new_folder = 'normalized_dataset_32x32/'

for fo in folders:
    path = folder_original + fo + '/'
    new_path = new_folder + fo + '/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    size = int(len(onlyfiles)* 0.2)
    test_files = random.sample(onlyfiles, size)
    for f in test_files:
        bashCommand = "cp " + path + f + " ./data/test/ ; rm " + path + f + ";"
        os.system(bashCommand)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print("here")
    for f in test_files:
        bashCommand = "cp " + path + f + " ./data/train/ ; rm " + path + f + ";"
        os.system(bashCommand)
