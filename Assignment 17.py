#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 02, 2019
#This program prompts the user for seconds



seconds = int(input("Enter number of seconds:"))

hours = int(seconds / 3600)

reaminingseconds = seconds % 3600

minutes = int(reaminingseconds / 60)

print("Hours:",hours)

print("Minutes:",minutes)

print("Seconds:",reaminingseconds)

 