#include <iostream>
using namespace std;

class MyPoint
{
public:
	void setPoint(int _x1, int _y1)
	{
		x1 = _x1;
		y1 = _y1;
	}
	int getX1()
	{
		return x1;
	}
	int getY1()
	{
		return y1;
	}
private:
	int x1;
	int y1;
}; 
class AdvCircle
{
public:
	void setCircle(int _r, int _x0, int _y0)
	{
		r = _r; x0 = _x0; y0 = _y0;
	}
public:
	int judge(MyPoint &myp)
	{
		int dd = (myp.getX1() - x0)*(myp.getX1() - x0) + (myp.getY1() - y0)*(myp.getY1() - y0);
			if (dd < r*r)
			{
				return 0;
			}
			else if (dd = r*r)
			{
				return 2;
			}
			else
			{
				return 1;
			}
	}
private:
	int r;
	int x0;
	int y0;
};

void main()
{
	AdvCircle c1;
	MyPoint p1;

	c1.setCircle(2, 3, 3);
	p1.setPoint(3, 5);
	//��Բ��1 ����Բ��0
	int tag = c1.judge(p1);
	if (tag == 1)
	{
		cout << "����Բ��" << endl;
	}
	else if(tag == 0)
	{
		cout << "����Բ��" << endl;
	}
	else 
	{
		cout << "����Բ��" << endl;
	}

	cout << "hollo..." << endl;
	system("pause");
	return;
}
