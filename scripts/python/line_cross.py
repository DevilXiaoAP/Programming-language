#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

class Point(object):
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def cross(p1, p2, p3):  # 叉积判定
    x1 = p2.x - p1.x
    y1 = p2.y - p1.y
    x2 = p3.x - p1.x
    y2 = p3.y - p1.y
    return x1 * y2 - x2 * y1

def line_extend(p1,p2):  #根据起始点和终止点，延长线段，70为延长横坐标70个像素点，为阈值可调
    # k = (y2 - y1) / (x2 - x1)
    # b = y1 - k * x1
    k = (-p1.y + p2.y) / (p1.x - p2.x)#因为坐标轴以左上角为起点
    b = (-p2.y) - k * p2.x
    if k < 0:
        x1 = p1.x + 70
        y1 = -(k * x1 + b)
        pe = Point(x1,y1)
    if k > 0:
        x1 = p1.x - 70
        y1 = -(k * x1 + b)
        pe = Point(x1,y1)
    return pe

def line_cross(p1, p2, p3, p4):  # 判断两线段是否相交
    """
    :param p1: 第一条线段的起始点
    :param p2: 第一条线段10帧之前的点
    :param p3:
    :param p4:
    :return: bool，是否相交
    """
    pe1 = line_extend(p1, p2)#第一条线段延长点
    pe2 = line_extend(p3, p4)#第二条线段延长点
    # 矩形判定，以l1、l2为对角线的矩形必相交，否则两线段不相交
    if (max(pe1.x, p2.x) >= min(pe2.x, p4.x)  # 矩形1最右端大于矩形2最左端
    #将两条线段表现成两个矩形框，初始判断是否香蕉
            and max(pe2.x, p4.x) >= min(pe1.x, p2.x)  # 矩形2最右端大于矩形1最左端
            and max(pe1.y, p2.y) >= min(pe2.y, p4.y)  # 矩形1最高端大于矩形2最低端
            and max(pe2.y, p4.y) >= min(pe1.y, p2.y)):  # 矩形2最高端大于矩形1最低端
        if (cross(pe1, p2, pe2) * cross(pe1, p2, p4) <= 0#利用叉积判断线段是否相交
                and cross(pe2, p4, pe1) * cross(pe2, p4, p2) <= 0):
            D = 1
        else:
            D = 0
    else:
        D = 0
    return D

# if __name__ == '__main__':
#
#         p1 = Point(1110, 525)
#         p2 = Point(1040, 495)
#         p3 = Point(1145, 510)
#         p4 = Point(1180, 460)
#
# d=line_cross(p1, p2, p3, p4)
# print("D=", d)
#
# d=line_extend(p1,p2)
# print("p=", d.x,d.y)
# t1 = time.time()
# for i in range(1000):
#     line_cross(p1, p2, p3, p4)
# t2 = time.time()
# print("cost time2:", 1000 * (t2 - t1), "ms")
