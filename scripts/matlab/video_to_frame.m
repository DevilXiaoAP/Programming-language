clc
clear all
fileName = 'C:\Users\Devil Xiao\Desktop\video5.mp4'; 
obj = VideoReader(fileName);
numFrames = obj.NumFrames ;% ֡������

 for k =  1 : 50 : numFrames % ��ȡ����
     frame = read(obj, k);
%      frame = imresize(frame,[436 1024],'bilinear');
     imwrite(frame,strcat('C:\Users\Devil Xiao\Desktop\dataset_right\',num2str(k+50),'.jpg'));% ����֡
 end