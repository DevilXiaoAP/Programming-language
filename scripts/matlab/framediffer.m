clc;clear all
fileName = 'C:\Users\Administrator\Desktop\2017_00819.mp4'; %MPEG-1 (.mpg), Windows Media Video (.wmv, .asf, .asx), 和任何Microsoft DirectShow?支持的类型。
obj = VideoReader(fileName);%读取视频软件
numFrames = obj.NumberOfFrames ;% 帧的总数
numFrames;
frame1=zeros();
frame2=zeros();
 for k = 1 :1: numFrames% 读取数据
     frame = read(obj, k);
     frame = rgb2gray(frame);%彩色图像转变为灰度图
     %imshow(frame);
     if mod(k,2)==0   %求的是k除以2的余数若恒等于0
        frame2 = frame;
     else
        frame1 = frame;
     end
     %imwrite(frame,strcat('D:\路面标识图片\20180724\2012_0124_230444_734\',num2str(k),'.jpg'));
     %imshow(frame);%显示帧
     sub = abs(frame2-frame1);%前后两帧图片求差值
         %开操作之后进行闭操作，开操作可以消除背景噪声，闭操作可以修复间断
     se = strel('disk',10);%3*3的空间滤波
     imgROI=imclose(sub,se);
     imgROI=imopen( imgROI,se);
     
     
     
     %grayvalue = graythresh(imgROI);%使用最大类间方差法找到图片的一个合适的阈值（grayvalue）。在使用im2bw函数将灰度图像转换为二值图像时，需要设定一个阈值，这个函数可以帮助我们获得一个合适的阈值。利用这个阈值通常比人为设定的阈值能更好地把一张灰度图像转换为二值图像。
     %graythresh%使用最大类间方差法来获得一个阈值.
     imgROI = imbinarize(sub,0.1); %函数的作用是把大于阈值的元素换成1，小于阈值的函数换成0。（二值图像输出）
     imgROI = bwmorph(imgROI,'open');%对二值图像进行数学形态学（Mathematical Morphology）运算
     imgROI = bwareaopen(imgROI,50);%Remove small objects from binary image删除二值图像BW中面积小于P的对象，默认情况下使用8邻域
 
   
   % imgROI=edge(imgROI,'canny');%算子进行边缘提取  roberts  sobel canny
     imgROI = im2uint8(imgROI);
% im2uint8用于将归一化到0～1之间（im2double 处理后的图像）转换为uint8类型
% uint8就是简单地把一个变量类型转换成uint8类型，数值大小不变 
% 如果对double处理之后的图像使用uint8()操作，返回值与原本的图像相同，不会出错。即im2uint8转换对应im2double 转换，数据有归一化过程；uint8对应double转换，转换过程中数值不发生变化。如果不能一一对应，则会出错。
%寻找像素为1的点 col为横坐标 row为纵坐标 
%f = find(imgROI~=0);%给出非零位置
%imgROI=find((0==I-1&&I == 1)||(0==I+1&&I == 1));          
     if (k>=3)
        montage = [frame,imgROI];
%     %adata=imread(difgrayFrame); 
        imshow(montage);
        imwrite(montage,strcat(' F:\out\',num2str(k),'.jpg'));
        %writeVideo(vidout,montage);
     end
 end