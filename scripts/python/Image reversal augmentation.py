#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/18
# @Author  : Devil_Xiao
# Purpose:Randomly enhance the color, brightness, and contrast of the original picture,
# and change the xml file accordingly, the option is whether to reverse the picture horizontally

from PIL import Image
import PIL.ImageEnhance as ImageEnhance
import xml.etree.ElementTree as ET
from tqdm import tqdm
import argparse
import os
import random


def random_image_enhancement(jpg_file, new_jpg, enhancement_scale, flip_horizontal=False):
    """对翻转的图片随机增强，enhancement_scale为在原图片基础上随即增减的比例系数
        flip_horizontal=False 只在原图上进行色彩，亮度以及对比度增强
        flip_horizontal=True 在原图的基础上进行翻转增强"""
    im = Image.open(jpg_file)
    scale = 1 + enhancement_scale * (random.uniform(-1, 1) / 10)
    image_random_brightness = ImageEnhance.Brightness(im).enhance(scale)
    image_random_Color = ImageEnhance.Color(image_random_brightness).enhance(scale)
    image_random_Contrast = ImageEnhance.Contrast(image_random_Color).enhance(scale)
    out = ImageEnhance.Sharpness(image_random_Contrast).enhance(scale)
    try:
        if flip_horizontal:
            out = out.transpose(Image.FLIP_LEFT_RIGHT)
    finally:
        out.save(new_jpg)


def flip_xml(xml_file, new_xml, image_width, image_format, flip_horizontal=False):
    """对xml标定物体的坐标进行水平翻转"""
    tree = ET.parse(xml_file)
    objs = tree.findall('object')
    filename = tree.find('filename')
    new_jpg = new_xml.replace(new_xml.split('\\')[-1].split('.')[0],
                              new_xml.split('\\')[-1].split('.')[0]).replace('xml', image_format)
    new_jpg_name = new_jpg.split('/')[-1]
    filename.text = new_jpg_name
    try:
        if flip_horizontal:
            for ix, obj in enumerate(objs):
                obj_new = obj.find('bndbox')
                xmin = str(image_width - int(obj_new.find('xmin').text))
                xmax = str(image_width - int(obj_new.find('xmax').text))
                obj_new.find('xmin').text = xmin
                obj_new.find('xmax').text = xmax
    finally:
        tree.write(new_xml)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=r'image/', help='image path')
    parser.add_argument('--suffix', type=str, default='_', help='The suffix added after the picture is reversed')
    parser.add_argument('--image_width', type=int, default='704', help='Flip the width of the picture horizontally')
    parser.add_argument('--enhancement_scale', type=int, default='2', help='Used as a scaling factor for augmentation')
    parser.add_argument('--flip_horizontal', type=bool, default=False, help='Whether to flip the original image')
    parser.add_argument('--image_format', type=str, default='jpg', help='Annotated image format')
    opt = parser.parse_args()
    print(opt)

    xml_files = [os.path.join(root_dir, file) for root_dir, _, files in os.walk(opt.path)
                 for file in files if(file.endswith('.xml'))]
    jpg_files = [xml_file.replace('xml', opt.image_format) for xml_file in xml_files]
    files = zip(jpg_files, xml_files)
    for jpg_file, xml_file in tqdm(files):
        new_jpg = jpg_file.replace(jpg_file.split('\\')[-1].split('.')[0],
                                   jpg_file.split('\\')[-1].split('.')[0] + opt.suffix)
        new_xml = new_jpg.replace(opt.image_format, 'xml')
        flip_xml(xml_file, new_xml, opt.image_width, opt.image_format, opt.flip_horizontal)
        random_image_enhancement(jpg_file, new_jpg, opt.enhancement_scale, opt.flip_horizontal)

