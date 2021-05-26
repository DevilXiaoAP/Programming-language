#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/17
# @Author  : Devil_Xiao
# Purpose:Divide and pack the files in the specified folder equally
import os
import zipfile
import argparse


def sort_key(s):
    """获取图片排序数字"""
    c = s.split('.')[0]
    return int(c)


def str_sort(alist):
    """返回按照关键字排序的列表"""
    alist.sort(key=sort_key)
    return alist


def dir_list(path_dir, Pack_in_order):
    """返回按数字大小排序完成的文件名"""
    list_row = [lists for lists in os.listdir(path_dir) if os.path.isfile(os.path.join(path_dir, lists))]
    if Pack_in_order:
        str_sort(list_row)
    return list_row


def make_zip(source_dir, sort_lists, output_filename):
    """打包文件夹内容为指定数段的文件"""
    zipf = zipfile.ZipFile(output_filename, 'w')
    for i, sort_list in enumerate(sort_lists, 1):
        pathfile = os.path.join(source_dir, sort_list)
        zipf.write(pathfile)
    zipf.close()


def batch_zip(source_dir, zip_nums, pack_in_order=True):
    """等分文件夹进行打包
    source_dir为目标文件夹
    zip_nums为等分个数"""
    sort_lists = dir_list(source_dir, pack_in_order)
    n = len(os.listdir(source_dir))
    file_num = n // zip_nums
    for i in range(zip_nums):
        make_zip(source_dir, sort_lists[i * file_num:(i+1) * file_num],
                 str(i+1) + '-' + str(file_num * i + 1) + '-' + str(file_num * (i + 1)) + '.zip')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=r'image/', help='image path')
    parser.add_argument('--zip_nums', type=int, default='11', help='number of equal divisions')
    parser.add_argument('--pack_in_order', type=bool, default=True, help='whether to pack in order')
    opt = parser.parse_args()
    print(opt)
    batch_zip(opt.path, opt.zip_nums, opt.pack_in_order)


