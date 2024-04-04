#include <iostream>
using namespace std;

class Person {
	int id;
	char name[100];

public:
	Person()
	{   
        cout << "Default constructor called" << endl; 
		cout << "Enter Id:";
		cin >> id;
		cout << "Enter Name:";
		cin >> name;
	}

	void display_person()
	{
		cout <<id << name <<endl;
	}

    ~Person(){
        cout<<"Destructor Called!";
    }
};

class Student : private Person {
	char course[50];
	int fee;

public:
	Student()
	{
		cout << "Default constructor called" << endl; 
		cout << "Enter the Course Name:";
		cin >> course;
		cout << "Enter the Course Fee:";
		cin >> fee;
	}

	void display_student()
	{
		display_p();
		cout <<course << fee << endl;
	}
    ~Student(){
        cout<<"Destructor of Student Class Called!"<<endl;
    }
};

int main()
{
	Student s;
	s.display_student();
	return 0;
}
