//Name:  Salma Elhassa
//Email: salma.elhassa52@myhunter.cuny.edu
//Date:  December 05, 2019

#include <iostream>

using namespace std;

int main()
{
	int row,column;//declaration of variables of row and column
	cout<<"Enter the Number of rows: ";
	cin>>row;//user inputting number of rows
	cout<<"Enter the Number of Columns: ";
	cin>>column;//user inputting number of columns
	for(int i=1;i<=row;i++)//this for loops will execute until i<=row
	{
	   for(int j=1;j<=column;j++)//this for loops will execute until i<=column
	   {
		cout<<((i+j+1)%2);
	   }
	   cout<<endl;
	}

	return 0;
}