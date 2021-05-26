
#include <iostream>
using namespace std;
class Test
{
public:
	Test(int a, int b) //---> Test(Test *this, int a, int b),this指向a的地址，将传递过来的实参赋值给形参再复制给Test.a
	{
		this->a = a;
		this-> b = b;	
	}
	void printT()
	{
		cout<<"a: " <<a <<endl;
		cout<< "b: " << this->b <<endl;
	}
protected:
private:
	int a;
	int b;
};

void main()
{
	
	Test t1(1, 2);//test initialize (&Test,1,2)
	t1.printT();// ===> printT(&t1)(直接使用此语句也可)
	cout<<"hello..."<<endl;
	system("pause");
	return ;
}