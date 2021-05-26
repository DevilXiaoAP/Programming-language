

% A=xlsread('21.xlsx');
% disp(A);
%[x]=xlsread("21.xlsx")

y = 7.778e-09*x.^5 - 1.158e-06*x.^4 + 6.629e-05*x.^3 - 0.001858*x.^2 + 0.02863*x + 0.6859;
p=plot(x,y,'-s','LineWidth',2,'LineSmoothing','on');
p.MarkerSize = 8;
p.MarkerIndices = 1:23:length(y);
hold on;


% % p1=plot(x1,y1,'-o','LineWidth',2,'LineSmoothing','on');
% % p1.MarkerSize = 7;
% % p1.MarkerIndices = 1:23:length(y);
% % hold on;

 
y2 = 1.129e-08*x2.^5 - 1.653e-06*x2.^4 + 9.204e-05*x2.^3 - 0.002461*x2.^2 + 0.03405*x2 + 0.7236
p2=plot(x2,y2,'-d','LineWidth',2,'LineSmoothing','on');
p2.MarkerSize = 6;
p2.MarkerIndices = 1:23:length(y);
hold on;

 
% y3= 1.515e-08*x3.^5 - 2.167e-06*x3.^4 + 0.0001172*x3.^3 - 0.002992*x3.^2 + 0.03742*x3 + 0.7343
% p3=plot(x3,y3,'-v','LineWidth',2,'LineSmoothing','on');
% p3.MarkerSize = 6;
% p3.MarkerIndices = 1:23:length(y);
% hold on;
% 
%  
%  y4 = 1.305e-08*x4.^5 - 1.91e-06*x4.^4 + 0.0001058*x4.^3 - 0.002763*x4.^2 + 0.03488*x4 + 0.7878
% p4=plot(x4,y4,'-+','LineWidth',2,'LineSmoothing','on');
% p4.MarkerSize = 6;
% p4.MarkerIndices = 1:23:length(y);
% hold on;

