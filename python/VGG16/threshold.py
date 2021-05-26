
import cv2 as cv
import numpy as np
src = cv.imread('C:/Users/Administrator/Desktop/love (2).png')
gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
# 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
ret,binary = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
print("threshold value %s" % ret)
cv.imshow("binary", binary)
cv.imwrite('2.1.jpg',cv.Canny(binary,30,100))