clc
clear all
fileName = 'C:\Users\Administrator\Desktop\�½��ļ��� (2)\2019���й��о�����ѧ��ģ����C��\����\����.mp4'; 
obj = VideoReader(fileName);
numFrames = obj.NumberOfFrames ;% ֡������
 for k = 1 :1: numFrames% ��ȡ����
     frame = read(obj, k);
     imwrite(frame,strcat('G:\��ģ\����\',num2str(k),'.jpg'));% ����֡
 end
    
