clc;clear all
fileName = 'C:\Users\Administrator\Desktop\2017_00819.mp4'; %MPEG-1 (.mpg), Windows Media Video (.wmv, .asf, .asx), ���κ�Microsoft DirectShow?֧�ֵ����͡�
obj = VideoReader(fileName);%��ȡ��Ƶ���
numFrames = obj.NumberOfFrames ;% ֡������
numFrames;
frame1=zeros();
frame2=zeros();
 for k = 1 :1: numFrames% ��ȡ����
     frame = read(obj, k);
     frame = rgb2gray(frame);%��ɫͼ��ת��Ϊ�Ҷ�ͼ
     %imshow(frame);
     if mod(k,2)==0   %�����k����2�������������0
        frame2 = frame;
     else
        frame1 = frame;
     end
     %imwrite(frame,strcat('D:\·���ʶͼƬ\20180724\2012_0124_230444_734\',num2str(k),'.jpg'));
     %imshow(frame);%��ʾ֡
     sub = abs(frame2-frame1);%ǰ����֡ͼƬ���ֵ
         %������֮����бղ������������������������������ղ��������޸����
     se = strel('disk',10);%3*3�Ŀռ��˲�
     imgROI=imclose(sub,se);
     imgROI=imopen( imgROI,se);
     
     
     
     %grayvalue = graythresh(imgROI);%ʹ�������䷽��ҵ�ͼƬ��һ�����ʵ���ֵ��grayvalue������ʹ��im2bw�������Ҷ�ͼ��ת��Ϊ��ֵͼ��ʱ����Ҫ�趨һ����ֵ������������԰������ǻ��һ�����ʵ���ֵ�����������ֵͨ������Ϊ�趨����ֵ�ܸ��õذ�һ�ŻҶ�ͼ��ת��Ϊ��ֵͼ��
     %graythresh%ʹ�������䷽������һ����ֵ.
     imgROI = imbinarize(sub,0.1); %�����������ǰѴ�����ֵ��Ԫ�ػ���1��С����ֵ�ĺ�������0������ֵͼ�������
     imgROI = bwmorph(imgROI,'open');%�Զ�ֵͼ�������ѧ��̬ѧ��Mathematical Morphology������
     imgROI = bwareaopen(imgROI,50);%Remove small objects from binary imageɾ����ֵͼ��BW�����С��P�Ķ���Ĭ�������ʹ��8����
 
   
   % imgROI=edge(imgROI,'canny');%���ӽ��б�Ե��ȡ  roberts  sobel canny
     imgROI = im2uint8(imgROI);
% im2uint8���ڽ���һ����0��1֮�䣨im2double ������ͼ��ת��Ϊuint8����
% uint8���Ǽ򵥵ذ�һ����������ת����uint8���ͣ���ֵ��С���� 
% �����double����֮���ͼ��ʹ��uint8()����������ֵ��ԭ����ͼ����ͬ�����������im2uint8ת����Ӧim2double ת���������й�һ�����̣�uint8��Ӧdoubleת����ת����������ֵ�������仯���������һһ��Ӧ��������
%Ѱ������Ϊ1�ĵ� colΪ������ rowΪ������ 
%f = find(imgROI~=0);%��������λ��
%imgROI=find((0==I-1&&I == 1)||(0==I+1&&I == 1));          
     if (k>=3)
        montage = [frame,imgROI];
%     %adata=imread(difgrayFrame); 
        imshow(montage);
        imwrite(montage,strcat(' F:\out\',num2str(k),'.jpg'));
        %writeVideo(vidout,montage);
     end
 end