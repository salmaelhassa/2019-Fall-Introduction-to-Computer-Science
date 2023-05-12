#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 07, 2019
#This program prompts the user for a list of names.

names = input("Please enter your list of names: ").split("; ")
print("\nYou entered:\n")
for x in names:
    tmp = x.split(", ")
    fn = tmp[0]
    ln = tmp[1]
    print(ln[0]+". "+fn)
print("\nThank you for using my name organizer")
