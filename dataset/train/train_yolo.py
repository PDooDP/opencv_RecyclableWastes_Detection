import os, random

# create folders
base = "VOCdevkit/VOC2021/"
images_path = os.path.join(base, "JPEGImages/")
train_it = os.path.join(base, "ImageSets/Main/train.txt")
val_it = os.path.join(base, "ImageSets/Main/val.txt")

file_list = os.listdir(images_path)
random.shuffle(file_list)
train_file = open(train_it, 'a')
val_file = open(val_it, 'a')

for index, file_obj in enumerate(file_list):
    file_path = os.path.join(images_path, file_obj)
    file_name, file_extend = os.path.splitext(file_obj)
    if(index >= len(file_list) * 0.2):
        train_file.write(file_name + "\n")
    else:
        val_file.write(file_name + "\n")

train_file.close()
val_file.close()
