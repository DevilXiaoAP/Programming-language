
#define  _CRT_SECURE_NO_WARNINGS 
#include <iostream>
using namespace std;

class Test
{
public:
	Test()  //�޲��� ���캯��
	{
		a = 10;  //������ɶ����Եĳ�ʼ������
		p = (char *)malloc(100);
		strcpy(p, "aaaaffff");
		cout<<"���ǹ��캯�� ��ִ����"<<endl;
	}
	void print()
	{
		cout<<p<<endl;
		cout<<a<<endl;
	}
	~Test() //�����������ͷſռ�
	{
		if (p != NULL)
		{
			free(p);
		}
		cout<<"������������,��������" <<endl;
	}
protected:
private:
	int a ;
	char *p;
};

//������һ����̨,�о��������Ϊ
void objplay()
{
	//�ȴ����Ķ��� ���ͷ�
	Test t1;
	t1.print();

	printf("�ָ���\n");
	Test t2;
	t2.print();
}
void main()
{
	objplay();
	cout<<"hello..."<<endl;
	system("pause");
	return ;
}