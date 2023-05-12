//Name:  Salma Elhassa
//Email: salma.elhassa52@myhunter.cuny.edu
//Date:  December 10, 2019

#include<iostream>
using namespace std;
int main()
{
   double amt,spent; // declare variable
   cout<<"Please enter the initial dollar amount: ";
   cin >> amt; // take input
   do{
       cout<<"Please enter the amount you spent: ";
       cin >> spent; // take amount spent input
       amt -= spent; // subtract spent from amount
       cout<<"You now have $"<<amt<<" remaining"<<endl;
   }while(amt>0); // check amount greater than 0
   cout<<"Your initial amount has been entirely spent";
   return 0;
}

