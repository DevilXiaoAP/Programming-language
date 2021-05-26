#include <opencv2/opencv.hpp>
#include <iostream>
#include <sstream>  
#include <direct.h>

using namespace std;
using namespace cv;

Mat org, dst, img, tmp;
static int  num = 362;//����ͼƬ��
int pic_size = 40;//��ȡͼƬ��߶�

void on_mouse(int event, int x, int y, int flags, void *ustc)//event����¼����ţ�x,y������꣬flags��ק�ͼ��̲����Ĵ���  
{
	static Point pre_pt = (-1, -1);//��ʼ����  
	static Point cur_pt = (-1, -1);//ʵʱ����  
	char temp[16];
	if (event == CV_EVENT_LBUTTONDOWN)//������£���ȡ��ʼ���꣬����ͼ���ϸõ㴦��Բ  
	{
		org.copyTo(img);//��ԭʼͼƬ���Ƶ�img��  
		sprintf(temp, "(%d,%d)", x, y);
		pre_pt = Point(x, y);
		putText(img, temp, pre_pt, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 0, 255), 1, 8);//�ڴ�������ʾ����  
		circle(img, pre_pt, 2, Scalar(255, 0, 0, 0), CV_FILLED, CV_AA, 0);//��Բ  
		imshow("img", img);
	}
	else if (event == CV_EVENT_MOUSEMOVE && !(flags & CV_EVENT_FLAG_LBUTTON))//���û�а��µ����������ƶ��Ĵ�����  
	{
		img.copyTo(tmp);//��img���Ƶ���ʱͼ��tmp�ϣ�������ʾʵʱ����  
		sprintf(temp, "(%d,%d)", x, y);
		cur_pt = Point(x, y);
		putText(tmp, temp, cur_pt, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 0, 255));//ֻ��ʵʱ��ʾ����ƶ�������  
		imshow("img", tmp);
	}
	else if (event == CV_EVENT_MOUSEMOVE && (flags & CV_EVENT_FLAG_LBUTTON))//�������ʱ������ƶ�������ͼ���ϻ�����  
	{
		img.copyTo(tmp);
		sprintf(temp, "(%d,%d)", x, y);
		cur_pt = Point(x, y);
		putText(tmp, temp, cur_pt, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 0, 255));
		rectangle(tmp, pre_pt, cur_pt, Scalar(0, 255, 0, 0), 1, 8, 0);//����ʱͼ����ʵʱ��ʾ����϶�ʱ�γɵľ���  
		imshow("img", tmp);
	}
	else if (event == CV_EVENT_LBUTTONUP)//����ɿ�������ͼ���ϻ�����  
	{
		org.copyTo(img);
		sprintf(temp, "(%d,%d)", x, y);

		//cur_pt.x = pre_pt.x + pic_size;
		//cur_pt.y = pre_pt.y + pic_size;
		cur_pt = Point(x, y);  //���Ҫ�Զ�����ƽ�ͼ��С����仰�Ϳ���,��Ϊ��ȡ������Ҫ�̶���С���������ﲻ��

		putText(img, temp, cur_pt, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 0, 255));
		circle(img, pre_pt, 2, Scalar(255, 0, 0, 0), CV_FILLED, CV_AA, 0);
		rectangle(img, pre_pt, cur_pt, Scalar(0, 0, 255, 0), 1, 8, 0);//���ݳ�ʼ��ͽ����㣬�����λ���img��  
		imshow("img", img);
		img.copyTo(tmp);
		//��ȡ���ΰ�Χ��ͼ�񣬲����浽dst��  
		int width = abs(pre_pt.x - cur_pt.x);
		int height = abs(pre_pt.y - cur_pt.y);
		if (width == 0 || height == 0)
		{
			printf("width == 0 || height == 0");
			return;
		}
		dst = org(Rect(min(cur_pt.x, pre_pt.x), min(cur_pt.y, pre_pt.y), width, height));
		namedWindow("dst");
		imshow("dst", dst);

		if (waitKey(0) == 's')
		{
			stringstream ss;
			string str;
			ss << "F:\\shujuji\\samples\\" << num << ".jpg";
			ss >> str;
			imwrite(str, dst);

			num++;

			cout << "����ͼƬ" << str << endl;
		}
		else
		{
			cout << "������" << endl;
		}

	}
}
void main()
{
	_mkdir("samples");
	string str1;
	for(int i = 93; i <= 170; i++)
	{
		stringstream ss1;
		ss1 << i;
		ss1 >> str1;
		string fileName = "F:\\shujuji\\yangben\\" + str1 + ".jpg";
		org = imread(fileName);
		org.copyTo(img);
		org.copyTo(tmp);
		namedWindow("img"); //����һ��img����
		
		//resizeWindow("img", 1080, 720);
		setMouseCallback("img", on_mouse, 0);//���ûص�����  
		imshow("img", img);
		if (waitKey(0) == '32')continue;
	}
}


