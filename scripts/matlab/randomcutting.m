clear all;
clc;
%ȡ��ͼƬ����
 Files=dir('F:\lingang\data\neg\orignel\*.jpg');
 N=length(Files);
 Names={};
for k = 1:N  
        B=imread(strcat('F:\lingang\data\neg\orignel\',num2str(k),'.jpg'));
        a=127;%�ü����
        b=127;%�ü�����
        c=20;%ÿ����Ƭ�ü�����
        %size(��һ���������ڶ�������)
        X=size(B,1); %��������--
        Y=size(B,2); %��������|
        for j= 1:c
          y=randperm(X-128,1);
          x=randperm(Y-128,1);
%           x=unidrnd(X-150,1,1);%������������
%           y=unidrnd(Y-150,1,1);%������������
          
          C=imcrop(B,[x y a b]);%���òü������ü�ͼ�����У���a,b����ʾ�ü������Ͻ�������ԭͼ���е�λ�ã�c��ʾ�ü���ͼ��Ŀ�d��ʾ�ü���ͼ��ĸ�
          % ���ھ�������[Xmin Ymin Width Height],Xmin�Ǻ����Xmin������,Ymin�������Ymin�����أ�
          % B = imresize(B,0.5,'bilinear');
          A=k*1000+j;
          imwrite(C,strcat('F:\lingang\data\neg\neg1\',num2str(A),'.jpg'));% ����֡
        end
end
