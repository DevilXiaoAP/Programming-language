clc
clear all
fileName = 'C:\Users\Devil Xiao\Desktop\video5.mp4'; 
obj = VideoReader(fileName);
numFrames = obj.NumFrames ;% 帧的总数

 for k =  1 : 50 : numFrames % 读取数据
     frame = read(obj, k);
%      frame = imresize(frame,[436 1024],'bilinear');
     imwrite(frame,strcat('C:\Users\Devil Xiao\Desktop\dataset_right\',num2str(k+50),'.jpg'));% 保存帧
 end