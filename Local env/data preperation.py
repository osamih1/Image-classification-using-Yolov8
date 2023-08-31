import os
import shutil

root_folder = "C:/Users/othma/Bureau/dataset"

categories = os.listdir(root_folder)

train_folder = os.path.join(root_folder,"train")
val_folder = os.path.join(root_folder,"val")
os.makedirs(train_folder)
os.makedirs(val_folder)

for category in categories:
    train_category_path = os.path.join(train_folder,category)
    val_category_path = os.path.join(val_folder, category)
    os.makedirs(train_category_path)
    os.makedirs(val_category_path)

    category_path = os.path.join(root_folder,category)
    category_images = os.listdir(category_path)

    split_limit = int(len(category_images) * 0.8)
    for category_image in category_images[:split_limit]:
        category_image_path_source = os.path.join(category_path,category_image)
        shutil.move(category_image_path_source,train_category_path)

    for category_image in category_images[split_limit:]:
        category_image_path_source = os.path.join(category_path,category_image)
        shutil.move(category_image_path_source,val_category_path)

    shutil.rmtree(category_path)