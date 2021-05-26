clc
clear all
fileName = 'C:\Users\Administrator\Desktop\新建文件夹 (2)\2019年中国研究生数学建模竞赛C题\附件\车辆.mp4'; 
obj = VideoReader(fileName);
numFrames = obj.NumberOfFrames ;% 帧的总数
 for k = 1 :1: numFrames% 读取数据
     frame = read(obj, k);
     imwrite(frame,strcat('G:\建模\车辆\',num2str(k),'.jpg'));% 保存帧
 end
    
