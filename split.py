
import os
import shutil
from tqdm import tqdm
import random

data = 'data'
train_data = 'train'
validation_data = 'validation'
test_data = 'test'

# Create a list containging all the .xyz files
# we will be working with
data_files = ...

# Split data_files into three different lists: one for training,
# validation, and testing
p_train = 0.7
p_val = 0.15
p_test = 0.15

n_train = int(p_train * len(data_files))
n_val = int(p_val * len(data_files))
n_test = int(p_test * len(data_files))

# Shuffle the data files
pass

# Split the data into the three subsets
train = data_files[:n_train]
validation = data_files[n_train:(n_train+n_val)]
test = data_files[(n_train+n_val):]

new_folders = [train_data, validation_data, test_data]
new_files = [train, validation, test]

# For each of the new folders, create it if it doesn't exist
pass

# For each of the files, copy the file into the new folder we
# created
for folder, files in zip(new_folders, new_files):
    for file in tqdm(files):
        shutil.copyfile(data + '/' + file, folder + '/' + file)
