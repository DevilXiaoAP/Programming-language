#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08
# @Author  : Devil_Xiao
# Purpose: This script is used to change the video_speed
# You can choose to specify the fps,
# or you can choose to change the multiple of the original playback speed

import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import argparse


def video_speed(video_root, out_root, fps=None, scale=1):
    """When fps and scale are specified at the same time, fps is the dominant"""
    cap = cv2.VideoCapture(video_root)
    video_width = int(cap.get(3))
    video_height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    if fps:
        videoWriter = cv2.VideoWriter(out_root, fourcc, fps, (video_width, video_height))
    else:
        fps = int(cap.get(cv2.CAP_PROP_FPS) * scale)
        videoWriter = cv2.VideoWriter(out_root, fourcc, fps, (video_width, video_height))
    flag = cap.isOpened()

    while (flag):
        flag, frame = cap.read()
        videoWriter.write(frame)
    videoWriter.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_name', type=str, default=r'C:\Users\Devil Xiao\Desktop\change_lane1.mp4', help='original video name')
    parser.add_argument('--result_name', type=str, default=r'C:\Users\Devil Xiao\Desktop\change_lane_result.mp4', help='result name')
    parser.add_argument('--fps', type=int, default=None, help='Specify the playback frame rate')
    parser.add_argument('--scale', type=float, default='0.5', help='Change the original video speed')
    opt = parser.parse_args()
    print(opt)
    video_speed(opt.video_name, opt.result_name, opt.fps, opt.scale)