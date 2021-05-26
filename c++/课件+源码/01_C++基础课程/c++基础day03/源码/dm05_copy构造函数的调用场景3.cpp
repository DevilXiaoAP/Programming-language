
#include <iostream>
using namespace std;


class Location 
{ 
public:
	Location( int xx = 0 , int yy = 0 ) 
	{ 
		X = xx ;  Y = yy ;  cout << "Constructor Object.\n" ; 
	}

	//copy构造函数  完成对象的初始化
	Location(const Location & obj) //copy构造函数 
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


//业务函数  形参是一个元素
void f(Location p)//用实参bcopy构造函数p，完成了对p的初始化
{
	cout<<p.GetX()<<endl;
}//p的内存最先释放，析构函数最先运行

void playobj()
{
	Location  a(1, 2);
	Location  b = a;
	cout<<"b对象已经初始化完毕"<<endl;

	f(b); //b实参取初始化形参p,会调用copy构造函数
}//p先释放析构函数，再到b释放析构函数，最后到a

void main()
{
	playobj();
	cout<<"hello..."<<endl;
	system("pause");
	return ;
}