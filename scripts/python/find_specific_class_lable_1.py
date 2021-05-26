#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/22
# @Author  : Devil_Xiao
# Purpose: This script is used to clean the data in the marked folder.
# In mode find_all=0, you can copy the marked pictures and annotations to a new folder.
# In mode find_all=1, you can copy pictures with specific category label to a new folder

import xml.etree.ElementTree as ET
from tqdm import tqdm
import argparse
import os
import shutil


def jpg_copy(old_jpgpath, new_jpgpath):
    shutil.copy(old_jpgpath, new_jpgpath)


def xml_copy(old_jpgpath, new_jpgpath):
    shutil.copy(old_jpgpath, new_jpgpath)


def file_copy(xml_file, new_xml_file):
    new_jpg_file = new_xml_file.replace('xml', 'jpg')
    tree = ET.parse(xml_file)
    jpg_files = xml_file.split('.')[0] + '.jpg'
    try:
        jpg_copy(jpg_files, new_jpg_file)
    except FileNotFoundError as e:
        os.remove(xml_file)
        print("there is no such file:" + jpg_files)
    else:
        xml_copy(xml_file, new_xml_file)
        tree = ET.parse(new_xml_file)
        tree.find('filename').text = new_jpg_file.split('/')[1]
        tree.find('path').text = new_jpg_file
        tree.write(new_xml_file)


def find_classes_xml(xml_file, new_xml_file, obj_classes, find_all=1):
    # find_all=0 仅将有标注的文件筛选到目标文件夹
    # find_all=1 将标注有目标类的文件筛选到目标文件夹
    if find_all == 0:
        file_copy(xml_file, new_xml_file)
    if find_all == 1:
        tree = ET.parse(xml_file)
        objs = tree.findall('object')
        for ix, obj in enumerate(objs):
            if obj.find('name').text in obj_classes:
                obj.find('name').text = 'chemicals vehicle'
                tree.write(xml_file)
                file_copy(xml_file, new_xml_file)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=r'chemical_vehicle//', help='image path')
    parser.add_argument('--obj_label', type=list, default=['chemicals vehicle'], help='The specific label to look for')
    parser.add_argument('--output_path', type=str, default='chemicals vehicle/', help='target output folder')
    parser.add_argument('--find_all', type=int, default='1', help='data filtering mode selection')
    opt = parser.parse_args()
    print(opt)

    if not os.path.exists(opt.output_path):
        os.makedirs(opt.output_path)

    xml_files = [os.path.join(root_dir, file) for root_dir, _, files in os.walk(opt.path)
                 for file in files if(file.endswith('.xml'))]

    for xml_file in tqdm(xml_files):
        new_xml = opt.output_path + str((len(os.listdir(opt.output_path))+1) // 2) + '.xml'
        find_classes_xml(xml_file, new_xml, opt.obj_label, opt.find_all)



