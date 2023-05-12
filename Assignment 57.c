//Name:  Salma Elhassa
//Email: salma.elhassa52@myhunter.cuny.edu
//Date:  December 06, 2019

#include<iostream>
using namespace std;

int main()
{
	double avgGrade;
	cout<<"Enter your average grade: ";
	cin>>avgGrade;
	if(avgGrade>=0 && avgGrade<60)
	{
	cout<<"Your letter grade is F";
	}
	else if(avgGrade>=60 && avgGrade<80)
	{
	cout<<"Your letter grade is C or D";
	}
	else if(avgGrade>=80 && avgGrade<90)
	{
	cout<<"Your letter grade is B";
	}
	else
	{
	cout<<"Your letter grade is A";
	}

return 0;
}