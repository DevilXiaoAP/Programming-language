clear;
clc;
%取样图片函数
 Files=dir('I:\subway\*.jpg');
 N=length(Files);
snum=25;%取样数
step=fix(N/snum);
Names={};
% Images={};

for k = 1:step:N  
    
        Names{k}=Files(k).name;
        B=imread(['I:\subway\' Names{k}]); 
       % B = imresize(B,0.5,'bilinear');
        path='F:\shujuji\yangben\'; 
        file=Files(k).name; 
        pathfile=fullfile(path,file); 
        imwrite(B,pathfile,'jpg');
end
