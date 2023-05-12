//Name:  Salma Elhassa
//Email: salma.elhassa52@myhunter.cuny.edu
//Date:  December 09, 2019

#include <iostream>

using namespace std;

int main() {
    double salary;
    while (true) {
        cout << "Please enter your salary: ";
        cin >> salary;
        if (salary > 0)
            break;
        cout << "Entered a negative number." << endl;
    }
    cout << "Your weekly salary is $" << salary << endl;
    return 0;
}