
#include <iostream>
using namespace std;


class Location 
{ 
public:
	Location( int xx = 0 , int yy = 0 ) 
	{ 
		X = xx ;  Y = yy ;  cout << "Constructor Object.\n" ; 
	}

	//copy���캯��  ��ɶ���ĳ�ʼ��
	Location(const Location & obj) //copy���캯�� 
	{
		X = obj.X; Y = obj.Y;
	}
	~Location() 
	{ 
		cout << X << "," << Y << " Object destroyed." << endl ; 
	}
	int  GetX () { return X ; }		int GetY () { return Y ; }
private :   int  X , Y ;
} ;


//ҵ����  �β���һ��Ԫ��
void f(Location p)//��ʵ��bcopy���캯��p������˶�p�ĳ�ʼ��
{
	cout<<p.GetX()<<endl;
}//p���ڴ������ͷţ�����������������

void playobj()
{
	Location  a(1, 2);
	Location  b = a;
	cout<<"b�����Ѿ���ʼ�����"<<endl;

	f(b); //bʵ��ȡ��ʼ���β�p,�����copy���캯��
}//p���ͷ������������ٵ�b�ͷ��������������a

void main()
{
	playobj();
	cout<<"hello..."<<endl;
	system("pause");
	return ;
}