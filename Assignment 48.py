#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: Novemeber 20, 2019

age = int(input('Enter your age: '))
while age < 0:
    print("You entered a negative number.  Try again.")
    age = int(input('Enter your age: '))
print("You entered:", age)