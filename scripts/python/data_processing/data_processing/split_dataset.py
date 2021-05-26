import shutil
import os
from tqdm import tqdm

img_path = 'F:/dataset/VehicleType/image/'
xml_path = 'F:/dataset/VehicleType/label/'
val_img_path = 'F:/dataset/VehicleType/image/val/'
val_label_path = 'F:/dataset/VehicleType/label/val/'

img_list = os.listdir(img_path)
val_img_list = []

for i in tqdm(range(1, 10840, 10)):
    s = str(i).zfill(6)

    for img in img_list:
        img = img.split(".", 1)
        val_img = img[0]
        if s == val_img:
            val_img_list.append(val_img)

for val_img in tqdm(val_img_list):
    shutil.move(img_path + val_img + '.jpg', val_img_path + val_img + '.jpg')
    shutil.move(xml_path + val_img + '.txt', val_label_path + val_img + '.txt')

