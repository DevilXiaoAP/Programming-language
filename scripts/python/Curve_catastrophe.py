#两条线段的夹角的计算，余弦定理
import math
import numpy as np
import time

#得到向量的坐标以及向量的模长
class Point(object):
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def vector(self):
        c = (self.x1 - self.x2, self.y1 - self.y2)
        return c

    def length(self):
        d = math.sqrt(pow((self.x1 - self.x2), 2) + pow((self.y1 - self.y2), 2))
        return d

#计算向量夹角
class Calculate(object):
    def __init__(self, x: object, y: object, m: object, n: object) -> object:#x,y表示量线段代表的向量，m,n代表模长
        self.x = x
        self.y = y
        self.m = m
        self.n = n

    def Vector_multiplication(self):
        self.mu = np.dot(self.x, self.y)#两线段的点积
        return self.mu

    def Vector_model(self):
        self.de = self.m * self.n
        return self.de

    def cal(self):
        result = Calculate.Vector_multiplication(self) / Calculate.Vector_model(self)#计算出的结果用余弦表示
        angle =math.acos(result)*57.3#(180/3.14)
        if angle > 20:#angle为两线段之间的夹角，此为阈值可调
         return angle #发生突变则输出角度
        else:
         return 0 #未发生突变则为1

if __name__ == '__main__':
    p1 = Point(1225, 288)#当前帧目标的坐标点
    p2 = Point(1254, 386)#5帧前目标的坐标点（可调）
    p3 = Point(1285, 312)#15帧前目标的坐标点，与当前帧两点合成一条线段（可调）
    p4 = Point(1223, 408)#20帧前目标的坐标点，与5帧前两点合成一条线段（可调）
    first_point = Line(p1.x, p1.y, p2.x, p2.y)
    two_point = Line(p3.x, p3.y, p4.x, p4.y)
    ca = Calculate(first_point.vector(), two_point.vector(), first_point.length(), two_point.length())
    print('两向量的夹角', ca.cal())


    # t1 = time.time()
    # for i in range (1000):
    #   ca = Calculate(first_point.vector(), two_point.vector(), first_point.length(), two_point.length())
    #   angle = math.acos(ca.cal()) * 57.3  # (180/3.14)
    # t2 = time.time()
    # print("cost time:",1000*(t2-t1),"ms")
