#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: November 05, 2019

binString = input("Enter binary number: ")
decNum = 0
for c in binString:
    decNum = decNum * 2
    if c == '1':
        decNum = decNum + 1
print("Your number in decimal is",decNum)