clear all;
clc;
%取样图片函数
 Files=dir('F:\lingang\data\neg\orignel\*.jpg');
 N=length(Files);
 Names={};
for k = 1:N  
        B=imread(strcat('F:\lingang\data\neg\orignel\',num2str(k),'.jpg'));
        a=127;%裁剪宽度
        b=127;%裁剪长度
        c=20;%每张照片裁剪数量
        %size(第一个行数，第二个列数)
        X=size(B,1); %横向列数--
        Y=size(B,2); %纵向列数|
        for j= 1:c
          y=randperm(X-128,1);
          x=randperm(Y-128,1);
%           x=unidrnd(X-150,1,1);%宽的随机数（）
%           y=unidrnd(Y-150,1,1);%宽的随机数（）
          
          C=imcrop(B,[x y a b]);%利用裁剪函数裁剪图像，其中，（a,b）表示裁剪后左上角像素在原图像中的位置；c表示裁剪后图像的宽，d表示裁剪后图像的高
          % 关于矩形区域[Xmin Ymin Width Height],Xmin是横向第Xmin个像素,Ymin是纵向第Ymin个像素；
          % B = imresize(B,0.5,'bilinear');
          A=k*1000+j;
          imwrite(C,strcat('F:\lingang\data\neg\neg1\',num2str(A),'.jpg'));% 保存帧
        end
end
