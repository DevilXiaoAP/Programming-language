
#include <iostream>
using namespace std;

class Fruit 
{
public:
	virtual void getFruit() = 0;

protected:
private:
};

class Banana : public Fruit
{
public:
	virtual void getFruit()
	{
		cout << "我是香蕉...." << endl;
	}
protected:
private:
};

class Apple : public Fruit
{
public:
	virtual void getFruit()
	{
		cout << "我是苹果...." << endl;
	}
protected:
private:
};


class Factory
{
public:
	Fruit *create(char *p)
	{

		if (strcmp(p, "banana") == 0)
		{
			return new Banana;	 
		}
		else if (strcmp(p, "apple") == 0)
		{
			return new Apple;
		}
		else
		{
			printf("不支持\n" ) ;
			return NULL;
		}
	}
};


void main()
{
	Factory *f = new Factory;

	Fruit *fruit = NULL;


	//工厂生产 香蕉
	fruit = f->create("banana");
	fruit->getFruit();
	delete fruit;


	fruit = f->create("apple");
	fruit->getFruit();
	delete fruit;

	delete f;
	cout<<"hello..."<<endl;
	system("pause");
	return ;
}