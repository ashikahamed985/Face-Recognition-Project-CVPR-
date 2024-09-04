import os
import shutil
import random
from pathlib import Path

# Path to the folder containing label-named folders
image_data_path = Path("imageData")

# Path to the new directory where train, valid, and test folders will be created
data_dir_path = Path("data_dir")
data_dir_path.mkdir(exist_ok=True)

# Create train, valid, and test folders inside data_dir if they don't exist
for folder_name in ["train", "valid", "test"]:
    (data_dir_path / folder_name).mkdir(exist_ok=True)

# Define the percentage of data for each set
train_percentage = 0.5
valid_percentage = 0.3
test_percentage = 0.2

# Loop through each label-named folder
for label_folder in os.listdir(image_data_path):
    label_folder_path = image_data_path / label_folder
    if not label_folder_path.is_dir():
        continue
    
    # List all files in the label folder
    files = os.listdir(label_folder_path)
    random.shuffle(files)  # Shuffle the files randomly
    
    # Split the files into train, valid, and test sets
    num_files = len(files)
    num_train = int(num_files * train_percentage)
    num_valid = int(num_files * valid_percentage)
    num_test = num_files - num_train - num_valid
    
    train_files = files[:num_train]
    valid_files = files[num_train:num_train + num_valid]
    test_files = files[num_train + num_valid:]
    
    # Move files to their respective folders
    for filename in train_files:
        src = label_folder_path / filename
        dest = data_dir_path / "train" / label_folder / filename
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
    
    for filename in valid_files:
        src = label_folder_path / filename
        dest = data_dir_path / "valid" / label_folder / filename
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
    
    for filename in test_files:
        src = label_folder_path / filename
        dest = data_dir_path / "test" / label_folder / filename
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
