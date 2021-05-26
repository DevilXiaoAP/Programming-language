clear;
clc;
%取样图片函数
 Files=dir('C:\Users\Administrator\Desktop\test\*.png');
 N=length(Files);
% snum=25;%取样数
% step=fix(N/snum);
Names={};
% Images={};

for k = 1:N  
    
        Names{k}=Files(k).name;
        B=imread(['C:\Users\Administrator\Desktop\test\' Names{k}]); 
        B = imresize(B,[436 1024],'bilinear');
        path='C:\Users\Administrator\Desktop\test1\'; 
        file=Files(k).name; 
        pathfile=fullfile(path,file); 
        imwrite(B,pathfile,'png');
end
